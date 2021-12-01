<?php

use humhub\modules\user\components\ActiveQueryUser;
use humhub\modules\user\models\User;
use humhub\widgets\LayoutAddons;

return [
    'id' => 'termsbox',
    'class' => 'humhub\modules\termsbox\Module',
    'namespace' => 'humhub\modules\termsbox',
    'events' => [
        ['class' => LayoutAddons::class, 'event' => LayoutAddons::EVENT_INIT, 'callback' => ['humhub\modules\termsbox\Events', 'onLayoutAddonsInit']],
        ['class' => User::class, 'event' => User::EVENT_CHECK_VISIBILITY, 'callback' => ['humhub\modules\termsbox\Events', 'onUserModelIsVisible']],
        ['class' => ActiveQueryUser::class, 'event' => ActiveQueryUser::EVENT_CHECK_VISIBILITY, 'callback' => ['humhub\modules\termsbox\Events', 'onUserQueryVisible']],
    ],
];
?>