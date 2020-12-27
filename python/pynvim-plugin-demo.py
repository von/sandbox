"""pynvim demo code

From: https://neovim.io/doc/user/remote_plugin.html with modifications

Must be saved in "rplugin/python3" in a 'runtimepath' directory
E.g. ~/.config/nvim/rplugin/python3/Limit.py

Then, the remote plugin manifest must be re-generated with
:UpdateRemotePlugins

See also:
    http://blog.tpleyer.de/posts/2019-02-20-Python-Plugin-for-Neovim.html
"""
import pynvim

@pynvim.plugin
class Limit(object):
    def __init__(self, vim):
        self.vim = vim
        self.calls = 0

    # use via 'map <leader>l :LimitCmd<CR'
    @pynvim.command('LimitCmd', range='', nargs='*', sync=True)
    def command_handler(self, args, range):
        self._increment_calls()
        self.vim.current.line = (
            'Command: Called %d times, args: %s, range: %s' % (self.calls,
                                                                args,
                                                                range))

    # Called whenever a python buffer is entered
    @pynvim.autocmd('BufEnter', pattern='*.py', eval='expand("<afile>")',
                    sync=True)
    def autocmd_handler(self, filename):
        self._increment_calls()
        self.vim.current.line = (
            'Autocmd: Called %s times, file: %s' % (self.calls, filename))

    # ':call LimitFunc()'
    @pynvim.function('LimitFunc')
    def function_handler(self, args):
        self._increment_calls()
        self.vim.current.line = (
            'Function: Called %d times, args: %s' % (self.calls, args))

    def _increment_calls(self):
        if self.calls == 5:
            raise Exception('Too many calls!')
        self.calls += 1
