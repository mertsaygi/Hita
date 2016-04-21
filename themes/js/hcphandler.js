BASE_URL = "http://127.0.0.1:8000/api/"

$("#gb").click(function(){
    $("#storage_unit_selection").html("GB");
});

$("#tb").click(function(){
    $("#storage_unit_selection").html("TB");
});

$("#tenant-form").submit(function(event) {

    event.preventDefault();

    var postData = {
        name: $('input[name*=tspace_name]').val(),
        systemVisibleDescription: "Created from management api",
        hardQuota : $('input[name*=tspace_hardQuota]').val()+" "+$("#storage_unit_selection").html(),
        softQuota : $('input[name*=tspace_softQuota]').val(),
        namespaceQuota : $('input[name*=tspace_namespaceQuota]').val(),
        complianceConfigurationEnabled : $('input[name*=complianceConfigurationEnabled]').val(),
        versioningConfigurationEnabled : $('input[name*=versioningConfigurationEnabled]').val(),
        searchConfigurationEnabled : $('input[name*=searchConfigurationEnabled]').val(),
        replicationConfigurationEnabled : $('input[name*=replicationConfigurationEnabled]').val(),
        servicePlanSelectionEnabled : $('input[name*=servicePlanSelectionEnabled]').val()
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

    var postData = {
        name: $('input[name*=nspace_name]').val(),
    };

    console.log(JSON.stringify(postData));
    console.log(BASE_URL+"create-tenant/");

    $.ajax({
    url : BASE_URL+"create-namespace/",
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify(postData),
    success: function(data, textStatus, jqXHR)
    {
        console.log(textStatus);
        console.log(jqXHR.status);
         var n = noty({
            text: 'Your namespace created successfully!',
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