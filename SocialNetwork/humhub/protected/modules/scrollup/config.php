<?php

namespace gm\humhub\modules\scrollup;

use humhub\widgets\LayoutAddons;

return [
    'id' => 'scrollup',
    'class' => Module::class,
    'namespace' => 'gm\humhub\modules\scrollup',
    'events' => [
        ['class' => LayoutAddons::class, 'event' => LayoutAddons::EVENT_INIT, 'callback' => [Events::class, 'onLayoutAddonsInit']],
    ]
];
?>