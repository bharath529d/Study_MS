    function checkAll(check_all_cb) {
        const other_cb = document.querySelectorAll('input[type="checkbox"]')
        other_cb.forEach(checkbox => {
            checkbox.checked = check_all_cb.checked
        });
    }

    function alert_message(message){
        alert(message);
    }
