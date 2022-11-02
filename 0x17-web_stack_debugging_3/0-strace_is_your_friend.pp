# Fix typo error in wordpress site running on apache2
exec { 'fix wordpress typo error':
	command => "sudo sed -i 's/phpp/php/g' /var/www/html/wp-settings.php; sudo service apache2 restart",
	path => ['/usr/local/bin', '/usr/local/sbin', '/sbin' , '/bin', '/usr/bin', '/usr/sbin']
}
