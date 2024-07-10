# 101-setup_web_static.pp
node default {
  # Ensure /data directory exists
  file { '/data':
    ensure => directory,
  }

  # Ensure /data/web_static directory exists
  file { '/data/web_static':
    ensure => directory,
  }

  # Ensure /data/web_static/releases directory exists
  file { '/data/web_static/releases':
    ensure => directory,
  }

  # Ensure /data/web_static/shared directory exists
  file { '/data/web_static/shared':
    ensure => directory,
  }

  # Ensure /data/web_static/releases/test directory exists
  file { '/data/web_static/releases/test':
    ensure => directory,
  }

  # Create /data/web_static/releases/test/index.html with the specified content
  file { '/data/web_static/releases/test/index.html':
    ensure  => file,
    content => "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>\n",
  }

  # Create a symbolic link /data/web_static/current pointing to /data/web_static/releases/test
  file { '/data/web_static/current':
    ensure => link,
    target => '/data/web_static/releases/test',
  }

  # Ensure Nginx is installed
  package { 'nginx':
    ensure => installed,
  }

  # Ensure Nginx service is running
  service { 'nginx':
    ensure     => running,
    enable     => true,
    hasrestart => true,
    require    => Package['nginx'],
  }

  # Configure Nginx to serve the content
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('nginx/default.erb'),
    notify  => Service['nginx'],
  }
}
