var tasks = {};
var progress_visible = false;
var last_mod = null;
var tr_table = {};

function render_row(mvs, type) {
    var row = $('<div class="mod row">');
    var mod;

    if($.isArray(mvs)) {
        mod = mvs[0];
    } else {
        mod = mvs;
        mvs = [mod];
    }

    if(type == 'available') {
        row.html($('#tpl-avail-mod').html());

        row.find('.install-btn').click(function (e) {
            e.preventDefault();

            fs2mod.install(mod.id, mod.version, []);
        });

        row.find('.info-btn').click(function (e) {
            e.preventDefault();

            fs2mod.showInfo(mod.id, mod.version);
        });
    } else if(type == 'installed') {
        row.html($('#tpl-installed-mod').html());

        row.find('.run-btn').click(function (e) {
            e.preventDefault();

            fs2mod.runMod(mod.id, mod.version);
        });
        row.find('.fred-btn').click(function (e) {
            e.preventDefault();

            fs2mod.runFredMod(mod.id, mod.version);
        });
        row.find('.settings-btn').click(function (e) {
            e.preventDefault();

            fs2mod.showSettings(mod.id, mod.version);
        });
        row.find('.del-btn').click(function (e) {
            e.preventDefault();

            fs2mod.uninstall(mod.id, mod.version, []);
        });
    } else if(type == 'updates') {
        row.html($('#tpl-update-mod').html());

        row.find('.update-btn').click(function (e) {
            e.preventDefault();

            fs2mod.updateMod(mod.id, mod.version);
        });
    }

    var logo = row.find('.mod-logo');
    if(logo.length > 0) {
        if(mod.logo) {
            logo.attr('src', 'file://' + mod.logo_path);
        } else {
            logo.replaceWith('<div class="no-logo">');
        }
    }

    row.find('.title').text(mod.title);
    return row;
}

function update_mods(mods, type) {
    $('#loading').hide();
    $('#mods').show();
    $('.info-page').hide();

    if(type == 'progress') {
        progress_visible = true;
        show_progress();
        return;
    } else {
        progress_visible = false;
    }

    var names = [];
    var mod_list = $('#mods').html('');

    $.each(mods, function (mid, info) {
        names.push([mid, info[0].title]);
    });

    names.sort(function (a, b) {
        return a[1] > b[1] ? 1 : (a[1] < b[1] ? -1 : 0);
    });

    names.forEach(function (item) {
        var mod = mods[item[0]];
        console.log(mod);
        mod_list.append(render_row(mod, type));
    });
}

function display_last(mod) {
    $('#loading, .info-page').hide();
    $('#mods').hide();

    var cont = $('#last-played');
    if(!mod) {
        $('#no-last-played').show();
        return;
    } else {
        cont.show();
    }

    cont.find('.run-btn').data('modid', mod.id);
    cont.find('.title').text(mod.title);

    if(mod.logo_path) {
        cont.find('.mod-logo').attr('src', 'file://' + mod.logo_path).show();
    } else {
        cont.find('.mod-logo').hide();
    }

    var desc = cont.find('.desc').text(mod.description);
    // Fix linebreaks
    desc.html(desc.html().replace(/\n/g, '<br>'));

    cont.show();
}

function _render_task(id, info) {
    var cont = $('<div class="mod">').html($('#tpl-dl-mod').html());
    cont.attr('id', 'task-' + id);

    cont.find('.abort-btn').click(function (e) {
        e.preventDefault();

        fs2mod.abortTask(id);
    });

    _update_task(cont, info);
    return cont;
}

function _update_task(cont, info) {
    var label = cont.find('.title');
    var prg_bar = cont.find('.master-prg');
    prg_bar.css('width', info.progress + '%');

    label.text(info.title);
    
    var sub_well = cont.find('.well');
    
    $.each(info.subs, function (i, sub) {
        var row = sub_well.find('.s-' + i);
        if(row.length == 0) {
            row = $('<div>').html('<span></span><br><div class="progress"><div class="progress-bar"></div></div>');
            row.addClass('s-' + i);
            sub_well.append(row);
        }

        if(sub[1] == 'Done' || sub[1] == 'Ready') {
            row.hide();
        } else {
            row.show();
            row.find('span').text(sub[1]);
            row.find('.progress-bar').css('width', (sub[0] * 100) + '%');
        }
    });
}

function add_task(id, text) {
    tasks[id] = { title: text, progress: 0, subs: [] };

    if(progress_visible) {
        $('#mods').append(_render_task(id, tasks[id]));
    }
}

function update_progress(id, percent, info, text) {
    tasks[id] = {
        progress: percent,
        subs: JSON.parse(info),
        title: text
    };

    if(progress_visible) {
        var task_cont = $('#task-' + id);
        if(task_cont.length == 0) {
            $('#mods').append(_render_task(id, tasks[id]));
        } else {
            _update_task(task_cont, tasks[id]);
        }
    }
}

function remove_task(id) {
    delete tasks[id];
    $('#task-' + id).remove();

    console.log(['Remove', id]);
}

function show_progress() {
    progress_visible = true;
    $('.info-page').hide();
    var modlist = $('#mods').empty().show();

    $.each(tasks, function (id, obj) {
        modlist.append(_render_task(id, obj));
    });
}

function load_translations(cb) {
    tr_table = {};
    var keys = get_translation_source();

    // Call fs2mod.tr() for each key
    var next = 0;
    function fetch() {
        if(next < keys.length) {
            var k = keys[next++];
            fs2mod.tr('modlist_ts', k, function (res) {
                tr_table[k] = res;
                fetch();
            });
        } else {
            cb();
        }
    }

    fetch();
}

function show_welcome() {
    $('.info-page, #mods, #loading').hide();
    $('#welcome').show();
}

function init() {
    $('.hide').removeClass('hide').hide();

    $('#last-played .run-btn').click(function (e) {
        e.preventDefault();

        fs2mod.runMod($(this).data('modid'), '');
    });

    load_translations(function () {
        $('div[data-tr], span[data-tr]').each(function () {
            var $this = $(this);
            $this.html(tr_table[$this.html()]);
        });

        $('#sel-fso').click(function (e) {
            e.preventDefault();

            fs2mod.selFs2path();
        });

        $('#gog-install').click(function (e) {
            e.preventDefault();

            fs2mod.runGogInstaller();
        });

        $('#tc-install').click(function (e) {
            e.preventDefault();

            fs2mod.enterTcMode();
        });

        $('a[target="_blank"]').click(function (e) {
            e.preventDefault();

            fs2mod.openExternal($(this).attr('href'));
        });
    });

    fs2mod.showWelcome.connect(show_welcome);
    fs2mod.showLastPlayed.connect(display_last);
    fs2mod.updateModlist.connect(update_mods);
    fs2mod.taskStarted.connect(add_task);
    fs2mod.taskProgress.connect(update_progress);
    fs2mod.taskFinished.connect(remove_task);

    fs2mod.finishInit();
}

if(window.qt) {
    new QWebChannel(qt.webChannelTransport, function (channel) {
        window.fs2mod = channel.objects.fs2mod;
        init();
    });
} else {
    $(init);
}