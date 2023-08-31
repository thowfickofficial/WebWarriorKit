import os
import subprocess

def install_dvwa():
    # Step 1: Update system packages
    print("Updating system packages...")
    subprocess.run(["sudo", "apt", "update"])

    # Step 2: Install required packages
    print("Installing required packages...")
    subprocess.run(["sudo", "apt", "install", "-y", "apache2", "mysql-server", "php", "php-mysql", "php-gd", "git"])

    # Step 3: Clone DVWA repository
    print("Cloning DVWA repository...")
    subprocess.run(["git", "clone", "https://github.com/ethicalhack3r/DVWA.git", "/var/www/html/dvwa"])

    # Step 4: Configure MySQL for DVWA
    print("Configuring MySQL for DVWA...")
    subprocess.run(["sudo", "mysql_secure_installation"])

    # Step 5: Create DVWA database
    subprocess.run(["sudo", "mysql", "-e", "CREATE DATABASE dvwa"])
    subprocess.run(["sudo", "mysql", "-e", "CREATE USER 'dvwa'@'localhost' IDENTIFIED BY 'password'"])
    subprocess.run(["sudo", "mysql", "-e", "GRANT ALL PRIVILEGES ON dvwa.* TO 'dvwa'@'localhost'"])
    subprocess.run(["sudo", "mysql", "-e", "FLUSH PRIVILEGES"])

    # Step 6: Configure DVWA
    print("Configuring DVWA...")
    subprocess.run(["sudo", "cp", "/var/www/html/dvwa/config/config.inc.php.dist", "/var/www/html/dvwa/config/config.inc.php"])
    subprocess.run(["sudo", "sed", "-i", "s/''/'dvwa'/", "/var/www/html/dvwa/config/config.inc.php"])
    subprocess.run(["sudo", "sed", "-i", "s/''/'password'/", "/var/www/html/dvwa/config/config.inc.php"])

    # Step 7: Set permissions
    subprocess.run(["sudo", "chown", "-R", "www-data:www-data", "/var/www/html/dvwa"])
    subprocess.run(["sudo", "chmod", "-R", "755", "/var/www/html/dvwa"])

    # Step 8: Restart Apache
    print("Restarting Apache...")
    subprocess.run(["sudo", "systemctl", "restart", "apache2"])

    print("DVWA installation completed.")
    
def install_bwapp():
    # Step 1: Install required packages (Apache, MySQL, PHP, Git)
    print("Installing required packages for bWAPP...")
    subprocess.run(["sudo", "apt", "install", "-y", "apache2", "mysql-server", "php", "php-mysql", "php-gd", "git"])

    # Step 2: Clone bWAPP repository
    print("Cloning bWAPP repository...")
    subprocess.run(["git", "clone", "https://github.com/ethicalhack3r/bWAPP.git", "/var/www/html/bwapp"])

    # Step 3: Configure MySQL for bWAPP
    print("Configuring MySQL for bWAPP...")
    subprocess.run(["sudo", "mysql", "-e", "CREATE DATABASE bwapp"])
    subprocess.run(["sudo", "mysql", "-e", "CREATE USER 'bwapp'@'localhost' IDENTIFIED BY 'password'"])
    subprocess.run(["sudo", "mysql", "-e", "GRANT ALL PRIVILEGES ON bwapp.* TO 'bwapp'@'localhost'"])
    subprocess.run(["sudo", "mysql", "-e", "FLUSH PRIVILEGES"])

    # Step 4: Set permissions
    subprocess.run(["sudo", "chown", "-R", "www-data:www-data", "/var/www/html/bwapp"])
    subprocess.run(["sudo", "chmod", "-R", "755", "/var/www/html/bwapp"])

    # Step 5: Restart Apache
    print("Restarting Apache...")
    subprocess.run(["sudo", "systemctl", "restart", "apache2"])

    print("bWAPP installation completed.")
    
def install_mutillidae():
    # Step 1: Install required packages
    print("Installing required packages for Mutillidae...")
    subprocess.run(["sudo", "apt", "install", "-y", "apache2", "mysql-server", "php", "php-mysql", "php-gd", "git"])

    # Step 2: Clone Mutillidae repository
    print("Cloning Mutillidae repository...")
    subprocess.run(["git", "clone", "https://github.com/webpwnized/mutillidae.git", "/var/www/html/mutillidae"])

    # Step 3: Configure MySQL for Mutillidae
    print("Configuring MySQL for Mutillidae...")
    subprocess.run(["sudo", "mysql", "-e", "CREATE DATABASE mutillidae"])
    subprocess.run(["sudo", "mysql", "-e", "CREATE USER 'mutillidae'@'localhost' IDENTIFIED BY 'password'"])
    subprocess.run(["sudo", "mysql", "-e", "GRANT ALL PRIVILEGES ON mutillidae.* TO 'mutillidae'@'localhost'"])
    subprocess.run(["sudo", "mysql", "-e", "FLUSH PRIVILEGES"])

    # Step 4: Set permissions
    subprocess.run(["sudo", "chown", "-R", "www-data:www-data", "/var/www/html/mutillidae"])
    subprocess.run(["sudo", "chmod", "-R", "755", "/var/www/html/mutillidae"])

    # Step 5: Restart Apache
    print("Restarting Apache...")
    subprocess.run(["sudo", "systemctl", "restart", "apache2"])

    print("Mutillidae installation completed.")
    
def install_webgoat():
    # Step 1: Install required packages
    print("Installing required packages for WebGoat...")
    subprocess.run(["sudo", "apt", "install", "-y", "openjdk-11-jre", "maven", "git"])

    # Step 2: Clone the WebGoat repository
    print("Cloning WebGoat repository...")
    subprocess.run(["git", "clone", "https://github.com/WebGoat/WebGoat.git", "/opt/WebGoat"])

    # Step 3: Build and start WebGoat
    print("Building and starting WebGoat...")
    os.chdir("/opt/WebGoat")
    subprocess.run(["mvn", "clean", "install", "-DskipTests"])
    subprocess.run(["mvn", "tomcat7:run-war"])

    print("WebGoat installation completed.")
    
def install_juiceshop():
    # Step 1: Install required packages
    print("Installing required packages for OWASP Juice Shop...")
    subprocess.run(["sudo", "apt", "install", "-y", "nodejs", "npm", "git"])

    # Step 2: Clone the OWASP Juice Shop repository
    print("Cloning OWASP Juice Shop repository...")
    subprocess.run(["git", "clone", "https://github.com/bkimminich/juice-shop.git", "/opt/juice-shop"])

    # Step 3: Install Juice Shop dependencies
    print("Installing Juice Shop dependencies...")
    os.chdir("/opt/juice-shop")
    subprocess.run(["npm", "install", "--production"])

    # Step 4: Start Juice Shop
    print("Starting OWASP Juice Shop...")
    subprocess.Popen(["npm", "start"])

    print("OWASP Juice Shop installation completed.")
    print("You can access Juice Shop at http://localhost:3000")

def main():
     # Display the tool name in figlet style
    subprocess.run(["figlet", "WebWarriorKit"])
    print("Select a web testing application to install:")
    print("1. DVWA (Damn Vulnerable Web Application)")
    print("2. bWAPP (Buggy Web Application)")
    print("3. Mutillidae")
    print("4. WebGoat")
    print("5. OWASP Juice Shop")
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        install_dvwa()
    elif choice == "2":
        install_bwapp()
    elif choice == "3":
        install_mutillidae()
    elif choice == "4":
        install_webgoat()
    
    elif choice == "5":
        install_juiceshop()
    else:
        print("Invalid choice. Please select a valid option.")
        


if __name__ == "__main__":
    main()