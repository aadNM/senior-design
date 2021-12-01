<?php

namespace gm\modules\weather;

use gm\modules\weather\Module;
use gm\modules\weather\Events;
use humhub\modules\admin\widgets\AdminMenu;
use humhub\modules\dashboard\widgets\Sidebar;
use humhub\modules\space\widgets\Sidebar as Spacebar;

return [
    'id' => 'weather',
    'class' => Module::class,
    'namespace' => 'gm\modules\weather',
    'events' => [
        ['class' => Sidebar::class, 'event' => Sidebar::EVENT_INIT, 'callback' => [Events::class, 'addWeatherFrame']],
        ['class' => Spacebar::class, 'event' => Spacebar::EVENT_INIT, 'callback' => [Events::class, 'addWeatherFrame']],
        ['class' => AdminMenu::class, 'event' => AdminMenu::EVENT_INIT, 'callback' => [Events::class,'onAdminMenuInit']],
    ]
];
