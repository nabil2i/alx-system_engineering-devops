# Puppet manifest to fix Too many open files
exec { 'fix-toomanyfiles':
    command => "sed -i 's/holberton hard nofile 5/holberton hard nofile 1048576/g' /etc/security/limits.conf; sed -i 's/holberton soft nofile 4/holberton soft nofile 1048576/g' /etc/security/limits.conf;
sed -i '$asession required pam_limits.so' /etc/pam.d/common-session; sed -i '$asession required pam_limits.so' /etc/pam.d/common-session-noninteractive ",
    path    => ['/bin', '/usr/bin', '/usr/sbin']
}
