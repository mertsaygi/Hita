BASE_URL = "http://127.0.0.1:8000/api/"

$("#tenant-form").submit(function(event) {

    event.preventDefault();

    var postData = {
        name: $('input[name*=tspace_name]').val(),
        systemVisibleDescription: "Created from management api",
        hardQuota : $('input[name*=tspace_hardQuota]').val(),
        softQuota : $('input[name*=tspace_softQuota]').val(),
        namespaceQuota : $('input[name*=tspace_namespaceQuota]').val()
    };

    console.log(JSON.stringify(postData));
    console.log(BASE_URL+"create-tenant/");

    $.ajax({
    url : BASE_URL+"create-tenant/",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify(postData),
    success: function(data, textStatus, jqXHR)
    {
        console.log(textStatus);
        console.log(jqXHR.status);
         var n = noty({
            text: 'Your tenant created successfully!',
            layout: 'top',
            type: 'success'
        });
    },
    error: function (jqXHR, textStatus, errorThrown)
    {
        console.log(textStatus);
        console.log(jqXHR);
        var n = noty({
            text: errorThrown+" "+jqXHR.responseText,
            layout: 'top',
            type: 'error'
        });
    }
    });

});

$("#namespace-form").submit(function(event) {

    event.preventDefault();

    var posting = $.post(url + "create-namespace", {
        name: $('input[name*=tspace_name]').val(),
        name2: $('input[name*=tspace_uname]').val()
    });

    posting.done(function(data) {
        var n = noty({
            text: 'Your namespace created successfully!',
            layout: 'top',
            type: 'success'
        });
    }).fail(function(xhr, textStatus, errorThrown) {
        var n = noty({
            text: xhr.statusText,
            layout: 'top',
            type: 'error'
        });
    });

});