(function () {
    function dismissAddAnotherPopup(win, newId, newRepr) {
        var name = windowname_to_id(win.name);
        var elem = document.getElementById(name);

        if (!elem) return;

        if (elem.tagName === 'SELECT') {
            var option = new Option(newRepr, newId, true, true);
            elem.options[elem.options.length] = option;
        } else if (elem.tagName === 'INPUT') {
            elem.value = newId;
        }

        // Trigger change event
        var event;
        if (typeof(Event) === 'function') {
            event = new Event('change', { bubbles: true });
        } else {
            event = document.createEvent('HTMLEvents');
            event.initEvent('change', true, true);
        }
        elem.dispatchEvent(event);

        win.close();
    }

    window.dismissAddAnotherPopup = dismissAddAnotherPopup;
})();