<?php
/**
 * HumHub DAV Access
 *
 * @package humhub.modules.humdav
 * @author KeudellCoding
 */

namespace humhub\modules\humdav;

use Yii;
use yii\helpers\Url;

class Module extends \humhub\components\Module {
    /**
     * @inheritdoc
     */
    public $resourcesPath = 'resources';
    
    /**
     * @inheritdoc
     */
    public function beforeAction($action) {
        Yii::$app->request->setBodyParams(null);

        return parent::beforeAction($action);
    }

    /**
     * @inheritdoc
     */
    public function getConfigUrl() {
        return Url::to(['/humdav/admin/index']);
    }
}
