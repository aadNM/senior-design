<?php

use humhub\modules\user\authclient\Collection;

return [
    'id' => 'auth-google',
    'class' => 'humhubContrib\auth\google\Module',
    'namespace' => 'humhubContrib\auth\google',
    'events' => [
        [Collection::class, Collection::EVENT_AFTER_CLIENTS_SET, ['humhubContrib\auth\google\Events', 'onAuthClientCollectionInit']]
    ],
];