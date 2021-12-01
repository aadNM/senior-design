<?php
/**
 * HumHub DAV Access
 *
 * @package humhub.modules.humdav
 * @author KeudellCoding
 */

use humhub\components\Application;
use humhub\components\ModuleManager;
use humhub\modules\directory\widgets\Menu as DirectoryMenu;
use humhub\modules\humdav\Events;
use humhub\widgets\TopMenu;

return [
    'id' => 'humdav',
    'class' => 'humhub\modules\humdav\Module',
    'namespace' => 'humhub\modules\humdav',
    'events' => [
        [ModuleManager::class, ModuleManager::EVENT_BEFORE_MODULE_DISABLE, [Events::class, 'onBeforeModuleDisable']],
        [Application::class, Application::EVENT_BEFORE_REQUEST, [Events::class, 'onBeforeRequest']],
        [TopMenu::class, TopMenu::EVENT_INIT, [Events::class, 'onTopMenuInit']],
        [DirectoryMenu::class, DirectoryMenu::EVENT_INIT, [Events::class, 'onDirectoryMenuInit']]
    ]
];
