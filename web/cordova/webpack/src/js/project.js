const host = 'http://localhost/casainteligente/web/';
const api = 'php/';
const init = function () {
    Project.navigate('control');
};

const Project = {
    init: init,
    load: function () {
        Project.host = localStorage.getItem('host') || host;
        Project.url = Project.host + api;
        $("form").on('submit', event => {
            const $this = $(event.currentTarget);
            event.preventDefault();
            Project.request($this.data('action'), $this.serializeArray(), 'POST').done(data => {
                if (typeof data.response === 'string') {
                    alert(data.response);
                }
                Project.navigate($this.data('redirect'), data);
            });
        });
    },
    navigate: function (file, data) {
        return $.get('pages/' + file + ".html", function (template) {
            const rendered = Mustache.render(template, data || {});
            $(".app").html(rendered);
            Project.setCookie('page', file, 1);
            Project.load();
        }, 'html');
    },
    request: function (uri, data, method) {
        if (!uri) return;
        return $.ajax(Project.url + uri, {
            method: method || 'GET',
            dataType: 'json',
            data: data,
            error: response => {
                if (response.responseJSON) {
                    const result = response.responseJSON;
                    switch (result.code) {
                        case 500:
                            console.error(result.error.message);
                            break;
                        case 400:
                            alert(result.error.message);
                            return;
                        default:
                            console.error(result);
                            break;
                    }
                } else if (response.responseText) {
                    console.error(`${Project.url} ${response.responseText}`);
                }
                alert('An error ocurred.');
            }
        });
    },
    setCookie: function (name, value, days) {
        var expires = "";
        if (days) {
            var date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toUTCString();
        }
        document.cookie = name + "=" + (value || "") + expires + "; path=/";
    },
    getCookie: function (name) {
        var nameEQ = name + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) == ' ') c = c.substring(1, c.length);
            if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
        }
        return null;
    },
    toast: function (options) {
        if (!options.type) options.type = "info";
        toastr[options.type](options.message, options.title, {timeOut: options.duration})
    }
};
module.exports = Project;