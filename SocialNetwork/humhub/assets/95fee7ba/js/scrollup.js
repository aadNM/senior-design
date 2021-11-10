humhub.module('scrollUpButton', function (module, require, $) {

    module.template = {
        scrollUpButton: '<a id="scrollUpButton"></a>'
    };

    var init = function () {
        var visible = false;

        var isSet = function (item) {
            return !(typeof item === 'undefined' || item === null);
        }
        var checkIfExist = function (item) {
            if (!isSet(item)) {
                return false;
            }
            return item.length > 0;
        }

        // @position can be either default or fromRight side
        function ParentElToAppend($parentEl, position = 'default') {
            this.$parentEl = $parentEl;
            this.position = position;
        }

        var getParentHtmlEl = function ($checkInArr) {
            if (!checkIfExist($checkInArr)) {
                return null;
            }
            var findFirstAcceptableElement = $checkInArr.find(el => checkIfExist(el.$parentEl));
            if (!isSet(findFirstAcceptableElement) || !checkIfExist(findFirstAcceptableElement.$parentEl)) {
                return null;
            }
            return findFirstAcceptableElement.$parentEl ? findFirstAcceptableElement.$parentEl : null
        }

        var $appendButtonTo = [
            new ParentElToAppend($('.layout-sidebar-container')),
            new ParentElToAppend($('.wiki-menu')),
            new ParentElToAppend($('.task-list')),
            new ParentElToAppend($('#wallStream')),
        ]

        if (!checkIfExist($appendButtonTo)) {
            return;
        }

        // var doesExit = checkIfExist();
        var $addTo = getParentHtmlEl($appendButtonTo);

        if (!$addTo) {
            return;
        }

        var $btn = initButton($addTo);
        var $window = $(window);
        $window.scroll(function () {
            var show = $window.scrollTop() > module.config.scrollTop;
            if (!visible && show) {
                $btn.addClass('show');
                visible = true;
            } else if (visible && !show) {
                $btn.removeClass('show');
                visible = false;
            }
        });
    };

    var initButton = function ($container) {
        var $btn = $(module.template.scrollUpButton)
            .css(module.config.buttonStyle)
            .on('click', function (e) {
                e.preventDefault();
                $('html, body').animate({scrollTop: 0});
            });

        $container.append($btn);

        if (!module.config.isCustomPosition) {
            if ($container.position === 'default') {
                var left = $container.offset().left + ($container.width() / 2) - ($btn.width() / 2);
                $btn.css({left: left + 'px'});
            } else { // fromRight
                var right = '5';
                $btn.css({right: right + '%'});
            }
        }

        return $btn;
    };

    var unload = function () {
        $('#scrollUpButton').remove();
    };

    module.export({
        initOnPjaxLoad: true,
        init: init,
        unload: unload
    });
});
