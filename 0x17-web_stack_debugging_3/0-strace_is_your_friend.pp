# Fixes typo error in wordpress site
exec { 'fix-typo-error':
  command => "sudo sed -i 's/phpp/php/g' /var/www/html/wp-settings.php; sudo service apache2 restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
