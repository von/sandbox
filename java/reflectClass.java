import java.lang.ClassLoader;
import java.lang.reflect.Constructor;
import java.lang.reflect.Method;

public class reflectClass {
    public static void main(String[] args) {
        try {
            String className = args[0];
            System.out.println("Class: " + className);
            ClassLoader cl = 
                new reflectClass().getClass().getClassLoader().getSystemClassLoader();
            Class targetClass = cl.loadClass(className);
            Constructor[] constructors = targetClass.getConstructors();
            for (int index = 0; index < constructors.length; index++)
            {
                System.out.println("Constructor: "
                                   + constructors[index].toString());
            }
            Method[] methods = targetClass.getMethods();
            for (int index = 0; index < methods.length; index++)
            {
                System.out.println("Method: " + methods[index].toString());
            }
        } catch (Exception e)
        {
            System.err.println("Error:" + e.getMessage());
        }
    }
}