<?php
/**
 * HumHub DAV Access
 *
 * @package humhub.modules.humdav
 * @author KeudellCoding
 */

namespace humhub\modules\humdav\components\sabre;

use Sabre\Uri;
use Sabre\DAV\PropPatch;
use Sabre\DAVACL\PrincipalBackend\AbstractBackend;
use humhub\modules\user\models\User;

class PrincipalBackend extends AbstractBackend {
    private static function getUserPrincipal(User $user) {
        return [
            'id' => $user->id,
			'uri' => 'principals/' . $user->username,
            '{DAV:}displayname' => $user->displayName,
            '{http://sabredav.org/ns}email-address' => $user->email
        ];
    }

    /**
     * @inheritdoc
     */
    public function getPrincipalsByPrefix($prefixPath) {
        $results = [];

        if ($prefixPath === 'principals') {
            foreach (User::findAll(['user.status' => User::STATUS_ENABLED]) as $user) {
                $results[] = self::getUserPrincipal($user);
            }
        }

        return $results;
    }

    /**
     * @inheritdoc
     */
    public function getPrincipalByPath($path) {
        list($prefix, $name) = Uri\split($path);

        if ($prefix === 'principals') {
            $user = User::findOne(['username' => $name]);
            if ($user !== null) {
				return self::getUserPrincipal($user);
            }
        }

        return null;
    }
    
    /**
     * @inheritdoc
     */
    public function updatePrincipal($path, PropPatch $propPatch) {
        $response = [
            403 => []
        ];
        
        foreach($propPatch as $key=>$value) {
            $response[403][$key] = null;
        }
        
        return $response;
    }

    /**
     * @inheritdoc
     */
    public function searchPrincipals($prefixPath, array $searchProperties, $test = 'allof') {
        return [];
    }

    /**
     * @inheritdoc
     */
    public function getGroupMemberSet($principal) {
        return [];
    }

    /**
     * @inheritdoc
     */
    public function getGroupMembership($principal) {
        return [];
    }

    /**
     * @inheritdoc
     */
    public function setGroupMemberSet($principal, array $members) {
        return false;
    }
}