# Puppet manifest to fix failed requests
exec { 'fix-failed-request':
    command => "sed -i 's/worker_processes 4;/worker_processes 9;/g' /etc/nginx/nginx.conf; sudo service nginx restart",
    path    => ['/bin', '/usr/bin', '/usr/sbin']
}
