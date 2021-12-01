<?php
/**
 * HumHub DAV Access
 *
 * @package humhub.modules.humdav
 * @author KeudellCoding
 */

namespace humhub\modules\humdav\components\sabre;

use humhub\modules\calendar\models\CalendarEntry;
use humhub\modules\humdav\definitions\VCalDefinitions;
use humhub\modules\space\models\Space;
use Yii;
use Sabre\CalDAV\Backend\AbstractBackend;
use humhub\modules\user\models\User;

class CalDavBackend extends AbstractBackend {
    /**
     * @inheritdoc
     */
    public function getCalendarsForUser($principalUri) {
        $username = Yii::$app->request->getAuthUser();
        $currentUser = User::findOne(['username' => $username]);
        if ($currentUser === null) {
            return [];
        }

        $results = [];

        if ($currentUser->isModuleEnabled('calendar')) {
            $results[] = [
                'id' => '0',
                'uri' => 'personal',
                'principaluri' => $principalUri,
                '{DAV:}displayname' => 'Profile calendar',
                '{http://sabredav.org/ns}read-only' => 1
            ];
        }

        foreach (Space::find()->all() as $space) {
            if (!$space->isModuleEnabled('calendar')) {
                continue;
            }

            // TODO: Make this optional
            if (!CalendarEntry::find()->contentContainer($space)->readable($currentUser)->exists()) {
                continue;
            }

            $results[] = [
                'id' => 'space_'.$space->id,
                'uri' => 'space_'.$space->url,
                'principaluri' => $principalUri,
                '{DAV:}displayname' => $space->getDisplayName(),
                '{http://sabredav.org/ns}read-only' => 1
            ];
        }

        return $results;
    }

    /**
     * @inheritdoc
     */
    public function createCalendar($principalUri, $calendarUri, array $properties) {
        throw new \Sabre\DAV\Exception\BadRequest('Not implemented yet!');
    }

    /**
     * @inheritdoc
     */
    public function updateCalendar($calendarId, \Sabre\DAV\PropPatch $propPatch) {
        throw new \Sabre\DAV\Exception\BadRequest('Not implemented yet!');
    }

    /**
     * @inheritdoc
     */
    public function deleteCalendar($calendarId) {
        throw new \Sabre\DAV\Exception\BadRequest('Not implemented yet!');
    }

    /**
     * @inheritdoc
     */
    public function getCalendarObjects($calendarId) {
        $results = [];
        $calendarEntries = [];
        
        $username = Yii::$app->request->getAuthUser();
        $currentUser = User::findOne(['username' => $username]);
        if ($currentUser === null) {
            return [];
        }
        
        if ($calendarId === '0') {
            $calendarEntries = CalendarEntry::find()->contentContainer($currentUser)->all();
        }
        else if (str_starts_with($calendarId, 'space_')) {
            $calendarEntries = $this->getSpaceCalendarObjects(substr($calendarId, strpos($calendarId, '_') + 1), $currentUser);
        }

        foreach ($calendarEntries as $calendarEntry) {
            $results[] = VCalDefinitions::getVCalDefinition($calendarEntry, $calendarId);
        }

        return $results;
    }

    /**
     * @inheritdoc
     */
    public function getCalendarObject($calendarId, $objectUri) {
        $objects = $this->getCalendarObjects($calendarId);
        foreach ($objects as $object) {
            if ($object['uri'] === $objectUri) {
                return $object;
            }
        }
        return false;
    }

    /**
     * @inheritdoc
     */
    public function createCalendarObject($calendarId, $objectUri, $calendarData) {
        throw new \Sabre\DAV\Exception\BadRequest('Not implemented yet!');
    }

    /**
     * @inheritdoc
     */
    public function updateCalendarObject($calendarId, $objectUri, $calendarData) {
        throw new \Sabre\DAV\Exception\BadRequest('Not implemented yet!');
    }

    /**
     * @inheritdoc
     */
    public function deleteCalendarObject($calendarId, $objectUri) {
        throw new \Sabre\DAV\Exception\BadRequest('Not implemented yet!');
    }

    // ==================================================================================================================

    private function getSpaceCalendarObjects(string $spaceId, User $currentUser) {
        $space = Space::findOne(['id' => $spaceId]);
        if ($space === null) {
            return [];
        }

        return CalendarEntry::find()->contentContainer($space)->readable($currentUser)->all();
    }
}