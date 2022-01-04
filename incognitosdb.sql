-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jan 04, 2022 at 10:28 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `incognitosdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `elgg_access_collections`
--

CREATE TABLE `elgg_access_collections` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `owner_guid` int(20) UNSIGNED NOT NULL,
  `subtype` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `elgg_access_collections`
--

INSERT INTO `elgg_access_collections` (`id`, `name`, `owner_guid`, `subtype`) VALUES
(3, 'friends', 40, 'friends');

-- --------------------------------------------------------

--
-- Table structure for table `elgg_access_collection_membership`
--

CREATE TABLE `elgg_access_collection_membership` (
  `user_guid` int(20) UNSIGNED NOT NULL,
  `access_collection_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `elgg_annotations`
--

CREATE TABLE `elgg_annotations` (
  `id` int(11) NOT NULL,
  `entity_guid` int(20) UNSIGNED NOT NULL,
  `name` text NOT NULL,
  `value` longtext NOT NULL,
  `value_type` enum('integer','text') NOT NULL,
  `owner_guid` int(20) UNSIGNED NOT NULL,
  `access_id` int(11) NOT NULL,
  `time_created` int(11) NOT NULL,
  `enabled` enum('yes','no') NOT NULL DEFAULT 'yes'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `elgg_api_users`
--

CREATE TABLE `elgg_api_users` (
  `id` int(11) NOT NULL,
  `api_key` varchar(40) DEFAULT NULL,
  `secret` varchar(40) NOT NULL,
  `active` int(11) DEFAULT 1
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `elgg_config`
--

CREATE TABLE `elgg_config` (
  `name` varchar(255) CHARACTER SET utf8 NOT NULL,
  `value` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `elgg_config`
--

INSERT INTO `elgg_config` (`name`, `value`) VALUES
('admin_registered', 'i:1;'),
('allowed_languages', 's:86:\"ca,hr,da,de,es,fi,fr,gl,el,id,it,ja,ko,cmn,nl,fa,pl,ro_ro,ru,gd,sr,sv,tr,cs,zh_hans,en\";'),
('allow_registration', 'b:1;'),
('allow_user_default_access', 'b:1;'),
('can_change_username', 'b:0;'),
('comments_latest_first', 'b:1;'),
('comments_per_page', 'i:25;'),
('comment_box_collapses', 'b:1;'),
('default_access', 'i:1;'),
('default_limit', 'i:10;'),
('disable_rss', 'b:0;'),
('email_html_part', 'b:1;'),
('email_html_part_images', 's:2:\"no\";'),
('enable_delayed_email', 'b:1;'),
('friendly_time_number_of_days', 'i:30;'),
('installed', 'i:1638340860;'),
('language', 's:2:\"en\";'),
('lastcache', 'i:1638342785;'),
('minusername', 'i:4;'),
('min_password_length', 'i:6;'),
('pagination_behaviour', 's:12:\"ajax-replace\";'),
('remove_branding', 'b:0;'),
('require_admin_validation', 'b:0;'),
('security_disable_password_autocomplete', 'b:0;'),
('security_email_require_confirmation', 'b:1;'),
('security_email_require_password', 'b:1;'),
('security_notify_admins', 'b:1;'),
('security_notify_user_admin', 'b:0;'),
('security_notify_user_ban', 'b:0;'),
('security_notify_user_password', 'b:1;'),
('security_protect_cron', 'b:0;'),
('security_protect_upgrade', 'b:1;'),
('session_bound_entity_icons', 'b:0;'),
('simplecache_enabled', 'i:0;'),
('simplecache_minify_css', 'b:1;'),
('simplecache_minify_js', 'b:1;'),
('system_cache_enabled', 'i:0;'),
('version', 'i:2017041200;'),
('walled_garden', 'b:1;'),
('__site_secret__', 's:32:\"zFqr8jda0R4h3SAxpDzAr2nzRrJrPgno\";');

-- --------------------------------------------------------

--
-- Table structure for table `elgg_delayed_email_queue`
--

CREATE TABLE `elgg_delayed_email_queue` (
  `id` int(11) UNSIGNED NOT NULL,
  `recipient_guid` bigint(20) UNSIGNED NOT NULL,
  `delivery_interval` varchar(255) NOT NULL,
  `data` mediumblob NOT NULL,
  `timestamp` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `elgg_entities`
--

CREATE TABLE `elgg_entities` (
  `guid` int(20) UNSIGNED NOT NULL,
  `type` enum('object','user','group','site') NOT NULL,
  `subtype` varchar(252) CHARACTER SET utf8 NOT NULL,
  `owner_guid` int(20) UNSIGNED NOT NULL,
  `container_guid` int(20) UNSIGNED NOT NULL,
  `access_id` int(11) NOT NULL,
  `time_created` int(11) NOT NULL,
  `time_updated` int(11) NOT NULL,
  `last_action` int(11) NOT NULL DEFAULT 0,
  `enabled` enum('yes','no') NOT NULL DEFAULT 'yes'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `elgg_entities`
--

INSERT INTO `elgg_entities` (`guid`, `type`, `subtype`, `owner_guid`, `container_guid`, `access_id`, `time_created`, `time_updated`, `last_action`, `enabled`) VALUES
(1, 'site', 'site', 0, 0, 2, 1638340860, 1638342949, 1638340860, 'yes'),
(2, 'object', 'plugin', 1, 1, 2, 1638340860, 1638340860, 1638340860, 'yes'),
(3, 'object', 'plugin', 1, 1, 2, 1638340860, 1638340860, 1638340860, 'yes'),
(4, 'object', 'plugin', 1, 1, 2, 1638340860, 1638340860, 1638340860, 'yes'),
(5, 'object', 'plugin', 1, 1, 2, 1638340860, 1638340860, 1638340860, 'yes'),
(6, 'object', 'plugin', 1, 1, 2, 1638340860, 1638340860, 1638340860, 'yes'),
(7, 'object', 'plugin', 1, 1, 2, 1638340860, 1638340860, 1638340860, 'yes'),
(8, 'object', 'plugin', 1, 1, 2, 1638340860, 1638340860, 1638340860, 'yes'),
(9, 'object', 'plugin', 1, 1, 2, 1638340860, 1638340860, 1638340860, 'yes'),
(10, 'object', 'plugin', 1, 1, 2, 1638340861, 1638340861, 1638340861, 'yes'),
(11, 'object', 'plugin', 1, 1, 2, 1638340861, 1638340861, 1638340861, 'yes'),
(12, 'object', 'plugin', 1, 1, 2, 1638340861, 1638340861, 1638340861, 'yes'),
(13, 'object', 'plugin', 1, 1, 2, 1638340861, 1638340861, 1638340861, 'yes'),
(14, 'object', 'plugin', 1, 1, 2, 1638340861, 1638340861, 1638340861, 'yes'),
(15, 'object', 'plugin', 1, 1, 2, 1638340861, 1638340861, 1638340861, 'yes'),
(16, 'object', 'plugin', 1, 1, 2, 1638340861, 1638340861, 1638340861, 'yes'),
(17, 'object', 'plugin', 1, 1, 2, 1638340861, 1638340861, 1638340861, 'yes'),
(18, 'object', 'plugin', 1, 1, 2, 1638340861, 1638340861, 1638340861, 'yes'),
(19, 'object', 'plugin', 1, 1, 2, 1638340861, 1638340861, 1638340861, 'yes'),
(20, 'object', 'plugin', 1, 1, 2, 1638340861, 1638340861, 1638340861, 'yes'),
(21, 'object', 'plugin', 1, 1, 2, 1638340861, 1638340861, 1638340861, 'yes'),
(22, 'object', 'plugin', 1, 1, 2, 1638340861, 1638340861, 1638340861, 'yes'),
(23, 'object', 'plugin', 1, 1, 2, 1638340861, 1638340861, 1638340861, 'yes'),
(24, 'object', 'plugin', 1, 1, 2, 1638340861, 1638340861, 1638340861, 'yes'),
(25, 'object', 'plugin', 1, 1, 2, 1638340861, 1638340861, 1638340861, 'yes'),
(26, 'object', 'plugin', 1, 1, 2, 1638340861, 1638340861, 1638340861, 'yes'),
(27, 'object', 'plugin', 1, 1, 2, 1638340861, 1638340861, 1638340861, 'yes'),
(28, 'object', 'plugin', 1, 1, 2, 1638340861, 1638340861, 1638340861, 'yes'),
(29, 'object', 'plugin', 1, 1, 2, 1638340861, 1638340861, 1638340861, 'yes'),
(30, 'object', 'plugin', 1, 1, 2, 1638340861, 1638340861, 1638340861, 'yes'),
(31, 'object', 'plugin', 1, 1, 2, 1638340861, 1638340861, 1638340861, 'yes'),
(32, 'object', 'plugin', 1, 1, 2, 1638340861, 1638340861, 1638340861, 'yes'),
(33, 'object', 'elgg_upgrade', 1, 1, 0, 1638340862, 1638340862, 1638340862, 'yes'),
(34, 'object', 'elgg_upgrade', 1, 1, 0, 1638340862, 1638340862, 1638340862, 'yes'),
(35, 'object', 'elgg_upgrade', 1, 1, 0, 1638340862, 1638340862, 1638340862, 'yes'),
(36, 'object', 'elgg_upgrade', 1, 1, 0, 1638340862, 1638340862, 1638340862, 'yes'),
(37, 'object', 'elgg_upgrade', 1, 1, 0, 1638340862, 1638340862, 1638340862, 'yes'),
(38, 'object', 'elgg_upgrade', 1, 1, 0, 1638340862, 1638340862, 1638340862, 'yes'),
(39, 'object', 'elgg_upgrade', 1, 1, 0, 1638340863, 1638340863, 1638340863, 'yes'),
(40, 'user', 'user', 0, 0, 2, 1638340948, 1638340948, 1641329400, 'yes'),
(41, 'object', 'widget', 40, 40, 2, 1638340948, 1638340948, 1638340948, 'yes'),
(42, 'object', 'widget', 40, 40, 2, 1638340948, 1638340948, 1638340948, 'yes'),
(43, 'object', 'widget', 40, 40, 2, 1638340948, 1638340948, 1638340948, 'yes'),
(44, 'object', 'widget', 40, 40, 2, 1638340948, 1638340948, 1638340948, 'yes'),
(45, 'object', 'widget', 40, 40, 2, 1638340948, 1638340948, 1638340948, 'yes');

-- --------------------------------------------------------

--
-- Table structure for table `elgg_entity_relationships`
--

CREATE TABLE `elgg_entity_relationships` (
  `id` int(11) NOT NULL,
  `guid_one` int(20) UNSIGNED NOT NULL,
  `relationship` varchar(255) NOT NULL,
  `guid_two` int(20) UNSIGNED NOT NULL,
  `time_created` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `elgg_entity_relationships`
--

INSERT INTO `elgg_entity_relationships` (`id`, `guid_one`, `relationship`, `guid_two`, `time_created`) VALUES
(1, 2, 'active_plugin', 1, 1638340861),
(2, 3, 'active_plugin', 1, 1638340861),
(3, 4, 'active_plugin', 1, 1638340861),
(4, 5, 'active_plugin', 1, 1638340861),
(5, 9, 'active_plugin', 1, 1638340861),
(6, 10, 'active_plugin', 1, 1638340861),
(7, 12, 'active_plugin', 1, 1638340861),
(8, 13, 'active_plugin', 1, 1638340861),
(9, 14, 'active_plugin', 1, 1638340861),
(10, 15, 'active_plugin', 1, 1638340861),
(11, 16, 'active_plugin', 1, 1638340861),
(12, 17, 'active_plugin', 1, 1638340862),
(13, 18, 'active_plugin', 1, 1638340862),
(15, 21, 'active_plugin', 1, 1638340862),
(17, 23, 'active_plugin', 1, 1638340862),
(18, 24, 'active_plugin', 1, 1638340862),
(19, 25, 'active_plugin', 1, 1638340862),
(20, 26, 'active_plugin', 1, 1638340862),
(21, 28, 'active_plugin', 1, 1638340862),
(22, 30, 'active_plugin', 1, 1638340862),
(23, 31, 'active_plugin', 1, 1638340862),
(24, 40, 'notify:email', 41, 1638340948),
(25, 40, 'notify:email', 42, 1638340948),
(26, 40, 'notify:email', 43, 1638340948),
(27, 40, 'notify:email', 44, 1638340948),
(28, 40, 'notify:email', 45, 1638340948),
(29, 27, 'active_plugin', 1, 1638342533),
(30, 7, 'active_plugin', 1, 1638342557),
(31, 8, 'active_plugin', 1, 1638342664),
(32, 11, 'active_plugin', 1, 1638342671),
(33, 19, 'active_plugin', 1, 1638342678),
(34, 32, 'active_plugin', 1, 1638342692);

-- --------------------------------------------------------

--
-- Table structure for table `elgg_hmac_cache`
--

CREATE TABLE `elgg_hmac_cache` (
  `hmac` varchar(255) CHARACTER SET utf8 NOT NULL,
  `ts` int(11) NOT NULL
) ENGINE=MEMORY DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `elgg_metadata`
--

CREATE TABLE `elgg_metadata` (
  `id` int(11) NOT NULL,
  `entity_guid` int(20) UNSIGNED NOT NULL,
  `name` text NOT NULL,
  `value` longtext NOT NULL,
  `value_type` enum('integer','text') NOT NULL,
  `time_created` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `elgg_metadata`
--

INSERT INTO `elgg_metadata` (`id`, `entity_guid`, `name`, `value`, `value_type`, `time_created`) VALUES
(1, 1, 'name', 'Incognito', 'text', 1638340860),
(2, 1, 'email', 'adoulazizdiallo@yahoo.fr', 'text', 1638340860),
(3, 2, 'title', 'activity', 'text', 1638340860),
(4, 3, 'title', 'blog', 'text', 1638340860),
(5, 4, 'title', 'bookmarks', 'text', 1638340860),
(6, 5, 'title', 'ckeditor', 'text', 1638340860),
(7, 6, 'title', 'custom_index', 'text', 1638340860),
(8, 7, 'title', 'dashboard', 'text', 1638340860),
(9, 8, 'title', 'developers', 'text', 1638340860),
(10, 9, 'title', 'discussions', 'text', 1638340860),
(11, 10, 'title', 'embed', 'text', 1638340861),
(12, 11, 'title', 'externalpages', 'text', 1638340861),
(13, 12, 'title', 'file', 'text', 1638340861),
(14, 13, 'title', 'friends', 'text', 1638340861),
(15, 14, 'title', 'friends_collections', 'text', 1638340861),
(16, 15, 'title', 'garbagecollector', 'text', 1638340861),
(17, 16, 'title', 'groups', 'text', 1638340861),
(18, 17, 'title', 'invitefriends', 'text', 1638340861),
(19, 18, 'title', 'likes', 'text', 1638340861),
(20, 19, 'title', 'login_as', 'text', 1638340861),
(21, 20, 'title', 'members', 'text', 1638340861),
(22, 21, 'title', 'messageboard', 'text', 1638340861),
(23, 22, 'title', 'messages', 'text', 1638340861),
(24, 23, 'title', 'pages', 'text', 1638340861),
(25, 24, 'title', 'profile', 'text', 1638340861),
(26, 25, 'title', 'reportedcontent', 'text', 1638340861),
(27, 26, 'title', 'search', 'text', 1638340861),
(28, 27, 'title', 'site_notifications', 'text', 1638340861),
(29, 28, 'title', 'system_log', 'text', 1638340861),
(30, 29, 'title', 'tagcloud', 'text', 1638340861),
(31, 30, 'title', 'thewire', 'text', 1638340861),
(32, 31, 'title', 'uservalidationbyemail', 'text', 1638340861),
(33, 32, 'title', 'web_services', 'text', 1638340861),
(34, 40, 'banned', 'no', 'text', 1638340948),
(35, 40, 'admin', 'yes', 'text', 1638340948),
(36, 40, 'language', 'en', 'text', 1638340948),
(37, 40, 'prev_last_action', '1641329399', 'integer', 1638340948),
(38, 40, 'last_login', '1641328943', 'integer', 1638340948),
(39, 40, 'prev_last_login', '1638595952', 'integer', 1638340948),
(40, 40, 'username', 'inconnue', 'text', 1638340948),
(41, 40, 'email', 'adoulazizdiallo@yahoo.fr', 'text', 1638340948),
(42, 40, 'name', 'NM', 'text', 1638340948),
(43, 40, 'password_hash', '$2y$10$zauyhbq5qdOamQSVa1Sb7uXBKtru/M4a0jQScISzkz4PF1PSyrt4S', 'text', 1638340948),
(44, 40, 'notification:default:email', '1', 'integer', 1638340948),
(45, 40, 'validated', '1', 'integer', 1638340948),
(46, 40, 'validated_method', 'admin_user', 'text', 1638340948),
(47, 40, 'validated_ts', '1638340948', 'integer', 1638340948),
(48, 40, 'first_login', '1638340948', 'integer', 1638340948),
(51, 1, 'description', '', 'text', 1638342132);

-- --------------------------------------------------------

--
-- Table structure for table `elgg_migrations`
--

CREATE TABLE `elgg_migrations` (
  `version` bigint(20) NOT NULL,
  `migration_name` varchar(100) DEFAULT NULL,
  `start_time` timestamp NULL DEFAULT NULL,
  `end_time` timestamp NULL DEFAULT NULL,
  `breakpoint` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `elgg_migrations`
--

INSERT INTO `elgg_migrations` (`version`, `migration_name`, `start_time`, `end_time`, `breakpoint`) VALUES
(20170728010000, 'RemoveSiteGuid', '2021-12-01 06:40:26', '2021-12-01 06:40:26', 0),
(20170728020000, 'MigrateDatalistsToConfig', '2021-12-01 06:40:26', '2021-12-01 06:40:26', 0),
(20170728030000, 'DenormalizeMetastrings', '2021-12-01 06:40:26', '2021-12-01 06:40:26', 0),
(20170728040000, 'ChangeTableEngine', '2021-12-01 06:40:26', '2021-12-01 06:40:26', 0),
(20170728050000, 'ExpandTextColumnsToLongtext', '2021-12-01 06:40:26', '2021-12-01 06:40:26', 0),
(20170728060000, 'RemoveLegacyPasswordHashes', '2021-12-01 06:40:26', '2021-12-01 06:40:26', 0),
(20170728072548, 'CreateAccessCollectionsTable', '2021-12-01 06:40:26', '2021-12-01 06:40:26', 0),
(20170728073540, 'CreateAccessCollectionMembershipTable', '2021-12-01 06:40:26', '2021-12-01 06:40:27', 0),
(20170728073706, 'CreateAnnotationsTable', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20170728074504, 'CreateApiUsersTable', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20170728074600, 'CreateEntitiesTable', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20170728074645, 'CreateEntityRelationshipsTable', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20170728074729, 'CreateEntitySubtypesTable', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20170728074757, 'CreateGeoCacheTable', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20170728074828, 'CreateGroupsEntityTable', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20170728074857, 'CreateHmacCacheTable', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20170728074925, 'CreateMetadataTable', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20170728074959, 'CreateObjectsEntityTable', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20170728075027, 'CreatePrivateSettingsTable', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20170728075056, 'CreateQueueTable', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20170728075129, 'CreateRiverTable', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20170728075155, 'CreateSitesEntityTable', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20170728075232, 'CreateSystemLogTable', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20170728075306, 'CreateUsersApiSessionsTable', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20170728075337, 'CreateUsersEntityTable', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20170728075418, 'CreateUsersRememberMeCookiesTable', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20170728075454, 'CreateUsersSessionsTable', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20170728075716, 'CreateConfigTable', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20170808084728, 'DropGeocodeCache', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20171006111953, 'DropSitesEntityTable', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20171006131622, 'DropGroupsEntityTable', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20171009115032, 'DropObjectsEntityTable', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20171010095648, 'DropUsersEntityTable', '2021-12-01 06:40:27', '2021-12-01 06:40:27', 0),
(20171016113827, 'UpdateMetadataColumns', '2021-12-01 06:40:27', '2021-12-01 06:40:28', 0),
(20171021111005, 'AddSubtypeIndexToRiverTable', '2021-12-01 06:40:28', '2021-12-01 06:40:28', 0),
(20171021111059, 'DenormalizeEntitySubtypes', '2021-12-01 06:40:28', '2021-12-01 06:40:28', 0),
(20171021111132, 'AlignSubtypeColumns', '2021-12-01 06:40:28', '2021-12-01 06:40:28', 0),
(20171106100916, 'AddAclSubtype', '2021-12-01 06:40:28', '2021-12-01 06:40:28', 0),
(20180109135052, 'DropTypeSubtypeFromRiverTable', '2021-12-01 06:40:28', '2021-12-01 06:40:28', 0),
(20180609152817, 'CreateSiteSecret', '2021-12-01 06:40:28', '2021-12-01 06:40:28', 0),
(20181107091651, 'AddEntitiesSubtypeIndex', '2021-12-01 06:40:28', '2021-12-01 06:40:28', 0),
(20190125082345, 'EntitiesAddTypeSubtypeIndex', '2021-12-01 06:40:28', '2021-12-01 06:40:28', 0),
(20190606111641, 'EntitiesAddTypeSubtypeContainerAndOwnerIndexes', '2021-12-01 06:40:28', '2021-12-01 06:40:28', 0),
(20191015125417, 'SetRiverEnabledToYes', '2021-12-01 06:40:28', '2021-12-01 06:40:28', 0),
(20200130161435, 'RemoveMetadataColumns', '2021-12-01 06:40:28', '2021-12-01 06:40:28', 0),
(20200130162616, 'RemoveRiverEnabledColumn', '2021-12-01 06:40:28', '2021-12-01 06:40:28', 0),
(20200303122949, 'AddTimeCreatedIndexToAnnotationsTable', '2021-12-01 06:40:28', '2021-12-01 06:40:28', 0),
(20200331083912, 'AddEntityGuidNameIndexToAnnotations', '2021-12-01 06:40:28', '2021-12-01 06:40:28', 0),
(20210225131119, 'IncreaseRelationshipColumnLength', '2021-12-01 06:40:28', '2021-12-01 06:40:29', 0),
(20210412110921, 'CreateDelayedEmailQueueTable', '2021-12-01 06:40:29', '2021-12-01 06:40:29', 0);

-- --------------------------------------------------------

--
-- Table structure for table `elgg_private_settings`
--

CREATE TABLE `elgg_private_settings` (
  `id` int(11) NOT NULL,
  `entity_guid` int(20) UNSIGNED NOT NULL,
  `name` varchar(128) NOT NULL,
  `value` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `elgg_private_settings`
--

INSERT INTO `elgg_private_settings` (`id`, `entity_guid`, `name`, `value`) VALUES
(1, 2, 'elgg:internal:priority', '1'),
(2, 3, 'elgg:internal:priority', '2'),
(3, 4, 'elgg:internal:priority', '3'),
(4, 5, 'elgg:internal:priority', '4'),
(5, 6, 'elgg:internal:priority', '5'),
(6, 7, 'elgg:internal:priority', '6'),
(7, 8, 'elgg:internal:priority', '7'),
(8, 9, 'elgg:internal:priority', '8'),
(9, 10, 'elgg:internal:priority', '9'),
(10, 11, 'elgg:internal:priority', '10'),
(11, 12, 'elgg:internal:priority', '11'),
(12, 13, 'elgg:internal:priority', '12'),
(13, 14, 'elgg:internal:priority', '13'),
(14, 15, 'elgg:internal:priority', '14'),
(15, 16, 'elgg:internal:priority', '15'),
(16, 17, 'elgg:internal:priority', '16'),
(17, 18, 'elgg:internal:priority', '17'),
(18, 19, 'elgg:internal:priority', '18'),
(19, 20, 'elgg:internal:priority', '19'),
(20, 21, 'elgg:internal:priority', '20'),
(21, 22, 'elgg:internal:priority', '21'),
(22, 23, 'elgg:internal:priority', '22'),
(23, 24, 'elgg:internal:priority', '23'),
(24, 25, 'elgg:internal:priority', '24'),
(25, 26, 'elgg:internal:priority', '25'),
(26, 27, 'elgg:internal:priority', '26'),
(27, 28, 'elgg:internal:priority', '27'),
(28, 29, 'elgg:internal:priority', '28'),
(29, 30, 'elgg:internal:priority', '29'),
(30, 31, 'elgg:internal:priority', '30'),
(31, 32, 'elgg:internal:priority', '31'),
(32, 33, 'id', 'core:2017080900'),
(33, 33, 'class', 'Elgg\\Upgrades\\AlterDatabaseToMultiByteCharset'),
(34, 33, 'title', 'core:upgrade:2017080900:title'),
(35, 33, 'description', 'core:upgrade:2017080900:description'),
(36, 33, 'offset', '0'),
(37, 33, 'is_completed', '1'),
(38, 34, 'id', 'core:2021040701'),
(39, 34, 'class', 'Elgg\\Upgrades\\ChangeUserNotificationSettingsNamespace'),
(40, 34, 'title', 'core:upgrade:2021040701:title'),
(41, 34, 'description', 'core:upgrade:2021040701:description'),
(42, 34, 'offset', '0'),
(43, 34, 'is_completed', '1'),
(44, 35, 'id', 'core:2021060401'),
(45, 35, 'class', 'Elgg\\Upgrades\\ContentOwnerSubscriptions'),
(46, 35, 'title', 'core:upgrade:2021060401:title'),
(47, 35, 'description', 'core:upgrade:2021060401:description'),
(48, 35, 'offset', '0'),
(49, 35, 'is_completed', '1'),
(50, 36, 'id', 'core:2020102301'),
(51, 36, 'class', 'Elgg\\Upgrades\\DeleteDiagnosticsPlugin'),
(52, 36, 'title', 'core:upgrade:2020102301:title'),
(53, 36, 'description', 'core:upgrade:2020102301:description'),
(54, 36, 'offset', '0'),
(55, 36, 'is_completed', '1'),
(56, 37, 'id', 'core:2021041901'),
(57, 37, 'class', 'Elgg\\Upgrades\\DeleteNotificationsPlugin'),
(58, 37, 'title', 'core:upgrade:2021041901:title'),
(59, 37, 'description', 'core:upgrade:2021041901:description'),
(60, 37, 'offset', '0'),
(61, 37, 'is_completed', '1'),
(62, 38, 'id', 'core:2021040801'),
(63, 38, 'class', 'Elgg\\Upgrades\\MigrateACLNotificationPreferences'),
(64, 38, 'title', 'core:upgrade:2021040801:title'),
(65, 38, 'description', 'core:upgrade:2021040801:description'),
(66, 38, 'offset', '0'),
(67, 38, 'is_completed', '1'),
(68, 39, 'id', 'core:2021022401'),
(69, 39, 'class', 'Elgg\\Upgrades\\NotificationsPrefix'),
(70, 39, 'title', 'core:upgrade:2021022401:title'),
(71, 39, 'description', 'core:upgrade:2021022401:description'),
(72, 39, 'offset', '0'),
(73, 39, 'is_completed', '1'),
(74, 33, 'start_time', '1638340863'),
(75, 33, 'completed_time', '1638340863'),
(76, 34, 'start_time', '1638340863'),
(77, 34, 'completed_time', '1638340863'),
(78, 35, 'start_time', '1638340863'),
(79, 35, 'completed_time', '1638340863'),
(80, 36, 'start_time', '1638340863'),
(81, 36, 'completed_time', '1638340863'),
(82, 37, 'start_time', '1638340863'),
(83, 37, 'completed_time', '1638340863'),
(84, 38, 'start_time', '1638340863'),
(85, 38, 'completed_time', '1638340863'),
(86, 39, 'start_time', '1638340863'),
(87, 39, 'completed_time', '1638340863'),
(88, 41, 'handler', 'control_panel'),
(89, 41, 'context', 'admin'),
(90, 41, 'column', '1'),
(91, 41, 'order', '0'),
(92, 42, 'handler', 'admin_welcome'),
(93, 42, 'context', 'admin'),
(94, 42, 'order', '10'),
(95, 42, 'column', '1'),
(96, 43, 'handler', 'online_users'),
(97, 43, 'context', 'admin'),
(98, 43, 'column', '2'),
(99, 43, 'order', '0'),
(100, 44, 'handler', 'new_users'),
(101, 44, 'context', 'admin'),
(102, 44, 'order', '10'),
(103, 44, 'column', '2'),
(104, 45, 'handler', 'content_stats'),
(105, 45, 'context', 'admin'),
(106, 45, 'order', '20'),
(107, 45, 'column', '2'),
(108, 13, 'friend_request', '1'),
(109, 16, 'hidden_groups', 'yes'),
(110, 16, 'limited_groups', 'yes'),
(111, 22, 'friends_only', '1'),
(112, 28, 'period', 'monthly'),
(113, 28, 'delete', 'yearly'),
(114, 8, 'display_errors', '0'),
(115, 8, 'screen_log', '0'),
(116, 8, 'show_strings', '0'),
(117, 8, 'wrap_views', '0'),
(118, 8, 'log_events', '0'),
(119, 8, 'show_gear', '1'),
(120, 8, 'show_modules', '0'),
(121, 8, 'block_email', ''),
(122, 8, 'forward_email', ''),
(123, 8, 'enable_error_log', '0');

-- --------------------------------------------------------

--
-- Table structure for table `elgg_queue`
--

CREATE TABLE `elgg_queue` (
  `id` int(11) NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 NOT NULL,
  `data` mediumblob NOT NULL,
  `timestamp` int(11) NOT NULL,
  `worker` varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `elgg_queue`
--

INSERT INTO `elgg_queue` (`id`, `name`, `data`, `timestamp`, `worker`) VALUES
(1, 'notifications', 0x433a34383a22456c67675c4e6f74696669636174696f6e735c537562736372697074696f6e4e6f74696669636174696f6e4576656e74223a3133343a7b4f3a383a22737464436c617373223a343a7b733a363a22616374696f6e223b733a31303a226d616b655f61646d696e223b733a393a226f626a6563745f6964223b693a34303b733a31313a226f626a6563745f74797065223b733a343a2275736572223b733a31343a226f626a6563745f73756274797065223b733a343a2275736572223b7d7d, 1638340948, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `elgg_river`
--

CREATE TABLE `elgg_river` (
  `id` int(11) NOT NULL,
  `action_type` varchar(32) NOT NULL,
  `view` text NOT NULL,
  `subject_guid` int(20) UNSIGNED NOT NULL,
  `object_guid` int(20) UNSIGNED NOT NULL,
  `target_guid` int(20) UNSIGNED NOT NULL,
  `annotation_id` int(11) NOT NULL,
  `posted` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `elgg_system_log`
--

CREATE TABLE `elgg_system_log` (
  `id` int(11) NOT NULL,
  `object_id` int(11) NOT NULL,
  `object_class` varchar(50) NOT NULL,
  `object_type` varchar(50) NOT NULL,
  `object_subtype` varchar(252) CHARACTER SET utf8 NOT NULL,
  `event` varchar(50) NOT NULL,
  `performed_by_guid` int(20) UNSIGNED NOT NULL,
  `owner_guid` int(20) UNSIGNED NOT NULL,
  `access_id` int(11) NOT NULL,
  `enabled` enum('yes','no') NOT NULL DEFAULT 'yes',
  `time_created` int(11) NOT NULL,
  `ip_address` varchar(46) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `elgg_system_log`
--

INSERT INTO `elgg_system_log` (`id`, `object_id`, `object_class`, `object_type`, `object_subtype`, `event`, `performed_by_guid`, `owner_guid`, `access_id`, `enabled`, `time_created`, `ip_address`) VALUES
(1, 46, 'ElggAdminNotice', 'object', 'admin_notice', 'delete', 40, 0, 0, 'yes', 1638341097, '127.0.0.1'),
(2, 51, 'ElggMetadata', 'metadata', 'description', 'create', 40, 0, 2, 'yes', 1638342132, '127.0.0.1'),
(3, 1, 'ElggSite', 'site', 'site', 'update', 40, 0, 2, 'yes', 1638342132, '127.0.0.1'),
(4, 1, 'ElggSite', 'site', 'site', 'update:after', 40, 0, 2, 'yes', 1638342132, '127.0.0.1'),
(5, 14, 'ElggRelationship', 'relationship', 'active_plugin', 'delete', 40, 0, 2, 'yes', 1638342509, '127.0.0.1'),
(6, 16, 'ElggRelationship', 'relationship', 'active_plugin', 'delete', 40, 0, 2, 'yes', 1638342517, '127.0.0.1'),
(7, 29, 'ElggRelationship', 'relationship', 'active_plugin', 'create', 40, 0, 2, 'yes', 1638342533, '127.0.0.1'),
(8, 30, 'ElggRelationship', 'relationship', 'active_plugin', 'create', 40, 0, 2, 'yes', 1638342557, '127.0.0.1'),
(9, 31, 'ElggRelationship', 'relationship', 'active_plugin', 'create', 40, 0, 2, 'yes', 1638342664, '127.0.0.1'),
(10, 32, 'ElggRelationship', 'relationship', 'active_plugin', 'create', 40, 0, 2, 'yes', 1638342671, '127.0.0.1'),
(11, 33, 'ElggRelationship', 'relationship', 'active_plugin', 'create', 40, 0, 2, 'yes', 1638342678, '127.0.0.1'),
(12, 34, 'ElggRelationship', 'relationship', 'active_plugin', 'create', 40, 0, 2, 'yes', 1638342692, '127.0.0.1'),
(13, 1, 'ElggSite', 'site', 'site', 'update', 40, 0, 2, 'yes', 1638342884, '127.0.0.1'),
(14, 1, 'ElggSite', 'site', 'site', 'update:after', 40, 0, 2, 'yes', 1638342884, '127.0.0.1'),
(15, 1, 'ElggSite', 'site', 'site', 'update', 40, 0, 2, 'yes', 1638342903, '127.0.0.1'),
(16, 1, 'ElggSite', 'site', 'site', 'update:after', 40, 0, 2, 'yes', 1638342903, '127.0.0.1'),
(17, 1, 'ElggSite', 'site', 'site', 'update', 40, 0, 2, 'yes', 1638342921, '127.0.0.1'),
(18, 1, 'ElggSite', 'site', 'site', 'update:after', 40, 0, 2, 'yes', 1638342921, '127.0.0.1'),
(19, 1, 'ElggSite', 'site', 'site', 'update', 40, 0, 2, 'yes', 1638342949, '127.0.0.1'),
(20, 1, 'ElggSite', 'site', 'site', 'update:after', 40, 0, 2, 'yes', 1638342949, '127.0.0.1'),
(21, 40, 'ElggUser', 'user', 'user', 'login:before', 0, 0, 2, 'yes', 1638435054, '127.0.0.1'),
(22, 39, 'ElggMetadata', 'metadata', 'prev_last_login', 'update', 40, 0, 2, 'yes', 1638435054, '127.0.0.1'),
(23, 39, 'ElggMetadata', 'metadata', 'prev_last_login', 'update:after', 40, 0, 2, 'yes', 1638435054, '127.0.0.1'),
(24, 38, 'ElggMetadata', 'metadata', 'last_login', 'update', 40, 0, 2, 'yes', 1638435054, '127.0.0.1'),
(25, 38, 'ElggMetadata', 'metadata', 'last_login', 'update:after', 40, 0, 2, 'yes', 1638435054, '127.0.0.1'),
(26, 40, 'ElggUser', 'user', 'user', 'login:before', 0, 0, 2, 'yes', 1638595881, '127.0.0.1'),
(27, 39, 'ElggMetadata', 'metadata', 'prev_last_login', 'update', 40, 0, 2, 'yes', 1638595881, '127.0.0.1'),
(28, 39, 'ElggMetadata', 'metadata', 'prev_last_login', 'update:after', 40, 0, 2, 'yes', 1638595881, '127.0.0.1'),
(29, 38, 'ElggMetadata', 'metadata', 'last_login', 'update', 40, 0, 2, 'yes', 1638595881, '127.0.0.1'),
(30, 38, 'ElggMetadata', 'metadata', 'last_login', 'update:after', 40, 0, 2, 'yes', 1638595881, '127.0.0.1'),
(31, 40, 'ElggUser', 'user', 'user', 'login:before', 0, 0, 2, 'yes', 1638595952, '127.0.0.1'),
(32, 39, 'ElggMetadata', 'metadata', 'prev_last_login', 'update', 40, 0, 2, 'yes', 1638595952, '127.0.0.1'),
(33, 39, 'ElggMetadata', 'metadata', 'prev_last_login', 'update:after', 40, 0, 2, 'yes', 1638595952, '127.0.0.1'),
(34, 38, 'ElggMetadata', 'metadata', 'last_login', 'update', 40, 0, 2, 'yes', 1638595952, '127.0.0.1'),
(35, 38, 'ElggMetadata', 'metadata', 'last_login', 'update:after', 40, 0, 2, 'yes', 1638595952, '127.0.0.1'),
(36, 40, 'ElggUser', 'user', 'user', 'login:before', 0, 0, 2, 'yes', 1641328943, '127.0.0.1'),
(37, 39, 'ElggMetadata', 'metadata', 'prev_last_login', 'update', 40, 0, 2, 'yes', 1641328943, '127.0.0.1'),
(38, 39, 'ElggMetadata', 'metadata', 'prev_last_login', 'update:after', 40, 0, 2, 'yes', 1641328943, '127.0.0.1'),
(39, 38, 'ElggMetadata', 'metadata', 'last_login', 'update', 40, 0, 2, 'yes', 1641328943, '127.0.0.1'),
(40, 38, 'ElggMetadata', 'metadata', 'last_login', 'update:after', 40, 0, 2, 'yes', 1641328943, '127.0.0.1');

-- --------------------------------------------------------

--
-- Table structure for table `elgg_users_apisessions`
--

CREATE TABLE `elgg_users_apisessions` (
  `id` int(11) NOT NULL,
  `user_guid` int(20) UNSIGNED NOT NULL,
  `token` varchar(40) DEFAULT NULL,
  `expires` int(11) NOT NULL
) ENGINE=MEMORY DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `elgg_users_remember_me_cookies`
--

CREATE TABLE `elgg_users_remember_me_cookies` (
  `code` varchar(32) NOT NULL,
  `guid` int(20) UNSIGNED NOT NULL,
  `timestamp` int(11) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `elgg_users_sessions`
--

CREATE TABLE `elgg_users_sessions` (
  `session` varchar(255) CHARACTER SET utf8 NOT NULL,
  `ts` int(11) UNSIGNED NOT NULL DEFAULT 0,
  `data` mediumblob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `elgg_users_sessions`
--

INSERT INTO `elgg_users_sessions` (`session`, `ts`, `data`) VALUES
('0bqevb0446cj65ugsnvipstkkf', 1638595952, 0x5f7366325f617474726962757465737c613a333a7b733a31343a225f5f656c67675f73657373696f6e223b733a32323a22686e6f4844587259314e66784f7163344a3442776f5f223b733a31303a225f656c67675f6d736773223b613a303a7b7d733a343a2267756964223b693a34303b7d5f7366325f6d6574617c613a333a7b733a313a2275223b693a313633383539353935323b733a313a2263223b693a313633383539353838393b733a313a226c223b733a313a2230223b7d5f73796d666f6e795f666c61736865737c613a303a7b7d),
('184h5fdinkv8gnj5isv0l50np5', 1638343438, 0x5f7366325f617474726962757465737c613a333a7b733a31343a225f5f656c67675f73657373696f6e223b733a32323a226665376c4b746b794a67302d7466465073375f622d67223b733a343a2267756964223b693a34303b733a31303a225f656c67675f6d736773223b613a303a7b7d7d5f7366325f6d6574617c613a333a7b733a313a2275223b693a313633383334333433373b733a313a2263223b693a313633383334303934383b733a313a226c223b733a313a2230223b7d),
('447og3eklbi5mllhsgb5m05o06', 1638435054, 0x5f7366325f617474726962757465737c613a323a7b733a31343a225f5f656c67675f73657373696f6e223b733a32323a2248447455646939664554664937546c5a3578624c7578223b733a343a2267756964223b693a34303b7d5f7366325f6d6574617c613a333a7b733a313a2275223b693a313633383433353035343b733a313a2263223b693a313633383433353034393b733a313a226c223b733a313a2230223b7d5f73796d666f6e795f666c61736865737c613a303a7b7d),
('6v9un9177pcohuvd2go2k4p0pf', 1638340948, 0x5f7366325f617474726962757465737c613a323a7b733a31343a225f5f656c67675f73657373696f6e223b733a32323a226665376c4b746b794a67302d7466465073375f622d67223b733a343a2267756964223b693a34303b7d5f73796d666f6e795f666c61736865737c613a303a7b7d5f7366325f6d6574617c613a333a7b733a313a2275223b693a313633383334303934383b733a313a2263223b693a313633383334303934383b733a313a226c223b733a313a2230223b7d),
('7ptn58cmmvjgefkcrk6dqaqco7', 1638596165, 0x5f7366325f617474726962757465737c613a343a7b733a31343a225f5f656c67675f73657373696f6e223b733a32323a22686e6f4844587259314e66784f7163344a3442776f5f223b733a31303a225f656c67675f6d736773223b613a303a7b7d733a343a2267756964223b693a34303b733a31323a22737469636b795f666f726d73223b613a303a7b7d7d5f7366325f6d6574617c613a333a7b733a313a2275223b693a313633383539363136343b733a313a2263223b693a313633383539353838393b733a313a226c223b733a313a2230223b7d),
('bfg2cll0ljf8r8sgfl980lunrm', 1641328943, 0x5f7366325f617474726962757465737c613a343a7b733a31343a225f5f656c67675f73657373696f6e223b733a32323a22735035384e7631646d634b383949755161616e505f57223b733a31373a226c6173745f666f72776172645f66726f6d223b733a35343a22687474703a2f2f6c6f63616c686f73742f696e636f676e69746f2d736974652f73657474696e67732f757365722f696e636f6e6e7565223b733a31303a225f656c67675f6d736773223b613a303a7b7d733a343a2267756964223b693a34303b7d5f7366325f6d6574617c613a333a7b733a313a2275223b693a313634313332383934333b733a313a2263223b693a313634313332383933343b733a313a226c223b733a313a2230223b7d5f73796d666f6e795f666c61736865737c613a303a7b7d),
('g8m13lbf88gsnm7e62p66f618o', 1641329397, 0x5f7366325f617474726962757465737c613a333a7b733a31343a225f5f656c67675f73657373696f6e223b733a32323a22735035384e7631646d634b383949755161616e505f57223b733a31303a225f656c67675f6d736773223b613a303a7b7d733a343a2267756964223b693a34303b7d5f7366325f6d6574617c613a333a7b733a313a2275223b693a313634313332393339363b733a313a2263223b693a313634313332383933343b733a313a226c223b733a313a2230223b7d),
('m49js5pdtn2t77drhlel6r30eq', 1638435822, 0x5f7366325f617474726962757465737c613a333a7b733a31343a225f5f656c67675f73657373696f6e223b733a32323a2248447455646939664554664937546c5a3578624c7578223b733a343a2267756964223b693a34303b733a31303a225f656c67675f6d736773223b613a303a7b7d7d5f7366325f6d6574617c613a333a7b733a313a2275223b693a313633383433353832323b733a313a2263223b693a313633383433353034393b733a313a226c223b733a313a2230223b7d),
('s1ls9adoct9e0u782fp4kiqvo5', 1638595881, 0x5f7366325f617474726962757465737c613a343a7b733a31343a225f5f656c67675f73657373696f6e223b733a32323a226a59674b475757363374684f4a383977414e5f796245223b733a31373a226c6173745f666f72776172645f66726f6d223b733a35343a22687474703a2f2f6c6f63616c686f73742f696e636f676e69746f2d736974652f746865776972652f6f776e65722f696e636f6e6e7565223b733a31303a225f656c67675f6d736773223b613a303a7b7d733a343a2267756964223b693a34303b7d5f7366325f6d6574617c613a333a7b733a313a2275223b693a313633383539353838313b733a313a2263223b693a313633383539353837373b733a313a226c223b733a313a2230223b7d5f73796d666f6e795f666c61736865737c613a303a7b7d);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `elgg_access_collections`
--
ALTER TABLE `elgg_access_collections`
  ADD PRIMARY KEY (`id`),
  ADD KEY `owner_guid` (`owner_guid`);

--
-- Indexes for table `elgg_access_collection_membership`
--
ALTER TABLE `elgg_access_collection_membership`
  ADD PRIMARY KEY (`user_guid`,`access_collection_id`);

--
-- Indexes for table `elgg_annotations`
--
ALTER TABLE `elgg_annotations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `entity_guid` (`entity_guid`),
  ADD KEY `name` (`name`(50)),
  ADD KEY `value` (`value`(50)),
  ADD KEY `owner_guid` (`owner_guid`),
  ADD KEY `access_id` (`access_id`),
  ADD KEY `time_created` (`time_created`),
  ADD KEY `entity_guid_name` (`entity_guid`,`name`(255));

--
-- Indexes for table `elgg_api_users`
--
ALTER TABLE `elgg_api_users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `api_key` (`api_key`);

--
-- Indexes for table `elgg_config`
--
ALTER TABLE `elgg_config`
  ADD PRIMARY KEY (`name`);

--
-- Indexes for table `elgg_delayed_email_queue`
--
ALTER TABLE `elgg_delayed_email_queue`
  ADD PRIMARY KEY (`id`),
  ADD KEY `recipient_guid` (`recipient_guid`),
  ADD KEY `delivery_interval` (`delivery_interval`),
  ADD KEY `recipient_interval` (`recipient_guid`,`delivery_interval`);

--
-- Indexes for table `elgg_entities`
--
ALTER TABLE `elgg_entities`
  ADD PRIMARY KEY (`guid`),
  ADD KEY `type` (`type`),
  ADD KEY `owner_guid` (`owner_guid`),
  ADD KEY `container_guid` (`container_guid`),
  ADD KEY `access_id` (`access_id`),
  ADD KEY `time_created` (`time_created`),
  ADD KEY `time_updated` (`time_updated`),
  ADD KEY `subtype` (`subtype`(50)),
  ADD KEY `type_subtype` (`type`,`subtype`(50)),
  ADD KEY `type_subtype_owner` (`type`,`subtype`(50),`owner_guid`),
  ADD KEY `type_subtype_container` (`type`,`subtype`(50),`container_guid`);

--
-- Indexes for table `elgg_entity_relationships`
--
ALTER TABLE `elgg_entity_relationships`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `guid_one` (`guid_one`,`relationship`,`guid_two`),
  ADD KEY `relationship` (`relationship`),
  ADD KEY `guid_two` (`guid_two`);

--
-- Indexes for table `elgg_hmac_cache`
--
ALTER TABLE `elgg_hmac_cache`
  ADD PRIMARY KEY (`hmac`),
  ADD KEY `ts` (`ts`);

--
-- Indexes for table `elgg_metadata`
--
ALTER TABLE `elgg_metadata`
  ADD PRIMARY KEY (`id`),
  ADD KEY `entity_guid` (`entity_guid`),
  ADD KEY `name` (`name`(50)),
  ADD KEY `value` (`value`(50));

--
-- Indexes for table `elgg_migrations`
--
ALTER TABLE `elgg_migrations`
  ADD PRIMARY KEY (`version`);

--
-- Indexes for table `elgg_private_settings`
--
ALTER TABLE `elgg_private_settings`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `entity_guid` (`entity_guid`,`name`),
  ADD KEY `name` (`name`),
  ADD KEY `value` (`value`(50));

--
-- Indexes for table `elgg_queue`
--
ALTER TABLE `elgg_queue`
  ADD PRIMARY KEY (`id`),
  ADD KEY `name` (`name`),
  ADD KEY `retrieve` (`timestamp`,`worker`);

--
-- Indexes for table `elgg_river`
--
ALTER TABLE `elgg_river`
  ADD PRIMARY KEY (`id`),
  ADD KEY `action_type` (`action_type`),
  ADD KEY `subject_guid` (`subject_guid`),
  ADD KEY `object_guid` (`object_guid`),
  ADD KEY `target_guid` (`target_guid`),
  ADD KEY `annotation_id` (`annotation_id`),
  ADD KEY `posted` (`posted`);

--
-- Indexes for table `elgg_system_log`
--
ALTER TABLE `elgg_system_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `object_id` (`object_id`),
  ADD KEY `object_class` (`object_class`),
  ADD KEY `object_type` (`object_type`),
  ADD KEY `object_subtype` (`object_subtype`),
  ADD KEY `event` (`event`),
  ADD KEY `performed_by_guid` (`performed_by_guid`),
  ADD KEY `access_id` (`access_id`),
  ADD KEY `time_created` (`time_created`),
  ADD KEY `river_key` (`object_type`,`object_subtype`,`event`(25));

--
-- Indexes for table `elgg_users_apisessions`
--
ALTER TABLE `elgg_users_apisessions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_guid` (`user_guid`),
  ADD KEY `token` (`token`);

--
-- Indexes for table `elgg_users_remember_me_cookies`
--
ALTER TABLE `elgg_users_remember_me_cookies`
  ADD PRIMARY KEY (`code`),
  ADD KEY `timestamp` (`timestamp`);

--
-- Indexes for table `elgg_users_sessions`
--
ALTER TABLE `elgg_users_sessions`
  ADD PRIMARY KEY (`session`),
  ADD KEY `ts` (`ts`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `elgg_access_collections`
--
ALTER TABLE `elgg_access_collections`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `elgg_annotations`
--
ALTER TABLE `elgg_annotations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `elgg_api_users`
--
ALTER TABLE `elgg_api_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `elgg_delayed_email_queue`
--
ALTER TABLE `elgg_delayed_email_queue`
  MODIFY `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `elgg_entities`
--
ALTER TABLE `elgg_entities`
  MODIFY `guid` int(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT for table `elgg_entity_relationships`
--
ALTER TABLE `elgg_entity_relationships`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `elgg_metadata`
--
ALTER TABLE `elgg_metadata`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;

--
-- AUTO_INCREMENT for table `elgg_private_settings`
--
ALTER TABLE `elgg_private_settings`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=124;

--
-- AUTO_INCREMENT for table `elgg_queue`
--
ALTER TABLE `elgg_queue`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `elgg_river`
--
ALTER TABLE `elgg_river`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `elgg_system_log`
--
ALTER TABLE `elgg_system_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `elgg_users_apisessions`
--
ALTER TABLE `elgg_users_apisessions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
