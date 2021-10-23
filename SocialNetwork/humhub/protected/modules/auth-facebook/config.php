<?php

use humhub\modules\user\authclient\Collection;

return [
    'id' => 'auth-facebook',
    'class' => 'humhubContrib\auth\facebook\Module',
    'namespace' => 'humhubContrib\auth\facebook',
    'events' => [
        [Collection::class, Collection::EVENT_AFTER_CLIENTS_SET, ['humhubContrib\auth\facebook\Events', 'onAuthClientCollectionInit']]
    ],
];
