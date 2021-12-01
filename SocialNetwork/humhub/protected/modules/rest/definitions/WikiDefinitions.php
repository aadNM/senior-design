<?php
/**
 * @link https://www.humhub.org/
 * @copyright Copyright (c) 2018 HumHub GmbH & Co. KG
 * @license https://www.humhub.com/licences
 */

namespace humhub\modules\rest\definitions;
use humhub\modules\wiki\models\WikiPage;
use humhub\modules\wiki\models\WikiPageRevision;
use yii\helpers\Url;


/**
 * Class WikiDefinitions
 *
 * @package humhub\modules\rest\definitions
 */
class WikiDefinitions
{
    public static function getWikiPage(WikiPage $page)
    {
        return [
            'id' => $page->id,
            'title' => $page->title,
            'is_home' => $page->is_home,
            'admin_only' => $page->admin_only,
            'is_category' => $page->is_category,
            'parent_page_id' => $page->parent_page_id,
            'permalink' => static::getPagePermalink($page),
            'latest_revision' => static::getWikiPageRevision($page->latestRevision),
            'content' => ContentDefinitions::getContent($page->content)
        ];
    }

    public static function getWikiPageRevision(WikiPageRevision $revision)
    {
        return [
            'id' => $revision->id,
            'revision' => $revision->revision,
            'is_latest' => $revision->is_latest,
            'wiki_page_id' => $revision->wiki_page_id,
            'created_by' => UserDefinitions::getUserShort($revision->author),
            'content' => $revision->content,
        ];
    }

    public static function getPagePermalink(WikiPage $page)
    {
        return Url::to(['/content/perma', 'id' => $page->content->id], true);
    }

}