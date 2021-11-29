<?php
/**
 * HumHub DAV Access
 *
 * @package humhub.modules.humdav
 * @author KeudellCoding
 */

namespace humhub\modules\humdav\definitions;

use humhub\modules\calendar\helpers\CalendarUtils;
use humhub\modules\calendar\interfaces\VCalendar;
use humhub\modules\calendar\models\CalendarEntry;

class VCalDefinitions {
    public static function getVCalDefinition(CalendarEntry $entry, $calendarId) {
        $vCal = strval(VCalendar::withEvents($entry, CalendarUtils::getSystemTimeZone(true))->serialize());
        return [
            'id' => $entry->id,
            'uri' => $entry->getUid().'.ics',
            'calendarid' => $calendarId,
            'calendardata' => $vCal,
            'size' => strlen($vCal),
            'etag' => '"'.md5($vCal).'"',
            'lastmodified' => $entry->getLastModified() !== null ? $entry->getLastModified()->getTimestamp() : (new \DateTime())->setTime(0, 0)->getTimestamp(),
            'component' => 'vevent'
        ];
    }
}
