<?php return array (
  'components' =>
  array (
    'db' =>
    array (
      'class' => 'yii\\db\\Connection',
      'dsn' => 'mysql:host=localhost;dbname=CCCSDT',
      'username' => 'ku-design',
      'password' => 'Young00528',
    ),
    'user' =>
    array (
    ),
    'mailer' =>
    array (
      'transport' =>
      array (
        'class' => 'Swift_MailTransport',
      ),
    ),
    'cache' =>
    array (
      'class' => 'yii\\caching\\FileCache',
      'keyPrefix' => 'humhub',
    ),
    'formatter' =>
    array (
      'defaultTimeZone' => 'America/Chicago',
    ),
  ),
  'params' =>
  array (
    'installer' =>
    array (
      'db' =>
      array (
        'installer_hostname' => 'localhost',
        'installer_database' => 'CCCSDT/.',
      ),
    ),
    'config_created_at' => 1634962701,
    'horImageScrollOnMobile' => '1',
    'databaseInstalled' => true,
    'installed' => true,
  ),
  'name' => 'socialnet',
  'language' => 'en-US',
  'timeZone' => 'America/Chicago',
); ?>
