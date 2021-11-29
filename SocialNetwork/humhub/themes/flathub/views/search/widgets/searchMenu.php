<?php

use yii\helpers\Url;
?>

<div class="topbar-bth dropdown search-menu">
    <a href="<?= Url::to(['/search/search/index']); ?>" id="search-menu" class="dropdown-toggle" aria-label="<?= Yii::t('SearchModule.views_search_index', 'Search for user, spaces and content') ?>">
        <i class="fa fa-search"></i>
    </a>
</div>

<script>
    /**
     * Open search menu
     */
    $('#search-menu-nav').click(function () {

        // use setIntervall to setting the focus
        var searchFocus = setInterval(setFocus, 10);

        function setFocus() {

            // set focus
            $('#search-menu-search').focus();
            // stop interval
            clearInterval(searchFocus);
        }

    })
</script>
