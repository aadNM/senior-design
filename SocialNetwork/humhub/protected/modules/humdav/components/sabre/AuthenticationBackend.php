<?php
/**
 * HumHub DAV Access
 *
 * @package humhub.modules.humdav
 * @author KeudellCoding
 */

namespace humhub\modules\humdav\components\sabre;

use Sabre\DAV\Auth\Backend\AbstractBasic;
use humhub\modules\user\models\forms\Login;

class AuthenticationBackend extends AbstractBasic {
    protected function validateUserPass($username, $password) {
        $login = new Login;

        if ($login->load(['username' => $username, 'password' => $password], '')  && $login->validate()) {
            return true;
        }

        return false;
    }
}

