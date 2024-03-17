import os
import subprocess

# Update system packages
subprocess.run(['yum', 'update', '-y'])

# Install required packages
subprocess.run(['yum', 'install', 'httpd', 'php-mysql', '-y'])

# Install PHP 7.3 using Amazon Linux Extras
subprocess.run(['amazon-linux-extras', 'install', '-y', 'php7.3'])

# Navigate to the web server root directory
os.chdir('/var/www/html')

# Create a file named 'healthy.html' with content 'healthy'
with open('healthy.html', 'w') as f:
    f.write('healthy')

# Download and extract the latest WordPress release
subprocess.run(['wget', 'https://wordpress.org/latest.tar.gz'])
subprocess.run(['tar', '-xzf', 'latest.tar.gz'])

# Copy WordPress files to web server root directory
subprocess.run(['cp', '-r', 'wordpress/*', '/var/www/html/'])

# Clean up downloaded files and directories
os.remove('latest.tar.gz')
subprocess.run(['rm', '-rf', 'wordpress'])

# Set permissions for wp-content directory
subprocess.run(['chmod', '-R', '755', 'wp-content'])
subprocess.run(['chown', '-R', 'apache:apache', 'wp-content'])

# Enable and start Apache HTTP server
subprocess.run(['chkconfig', 'httpd', 'on'])
subprocess.run(['systemctl', 'enable', 'httpd'])
subprocess.run(['service', 'httpd', 'start'])