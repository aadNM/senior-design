<?php
/**
 * HumHub DAV Access
 *
 * @package humhub.modules.humdav
 * @author KeudellCoding
 */

namespace humhub\modules\humdav\models\sabre;

use Sabre\DAVACL\ACLTrait;
use Sabre\DAVACL\IACL;

class AddressBookRoot extends \Sabre\CardDAV\AddressBookRoot implements IACL {
    
    use ACLTrait;

    /**
     * @inheritdoc
     */
    function getACL() {
        return [
            [
                'privilege' => '{DAV:}read',
                'principal' => '{DAV:}authenticated',
                'protected' => true
            ]
        ];
    }

    /**
     * @inheritdoc
     */
    function getChildForPrincipal(array $principal) {
        return new AddressBookHome($this->carddavBackend, $principal['uri']);
    }
}