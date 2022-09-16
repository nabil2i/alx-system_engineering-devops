# install flask from pip3

package { 'pip3 flask':
  ensure   => '2.1.0',
  provider => 'gem',
}
