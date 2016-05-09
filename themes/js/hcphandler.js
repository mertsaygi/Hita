
PROD_URL = "https://192.241.219.84/"

DEV_URL = "https://192.241.219.84/"

BASE_URL = PROD_URL+"api/"

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
        servicePlanSelectionEnabled : $('input[name*=servicePlanSelectionEnabled]').val()
    };

    console.log(JSON.stringify(postData));
    console.log(BASE_URL+"tenant/create/");

    $.ajax({
    url : BASE_URL+"tenant/create/",
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
        "description" : "Created for the Finance department at Example Company by Lee Green",
        "hashScheme" : "SHA-256",
        "enterpriseMode" : true,
        hardQuota : $('input[name*=nspace_hardQuota]').val()+" "+$("#storage_unit_selection").html(),
        softQuota : $('input[name*=nspace_softQuota]').val(),
        "versioningSettings" : {
            "enabled" : true,
            "prune" : true,
            "pruneDays" : 10,
        },
        "aclsUsage" : "ENABLED",
        "searchEnabled" : true,
        "indexingEnabled" : true,
        "customMetadataIndexingEnabled" : true,
        "replicationEnabled" : true,
        "readFromReplica" : true,
        "serviceRemoteSystemRequests" : true,
        "tags" : {
            "tag" : [ "Billing", "lgreen" ]
        }
    };

    console.log(JSON.stringify(postData));
    console.log(BASE_URL+"namespace/create/"+$('input[name*=nspace_container]').val());

    $.ajax({
    url : BASE_URL+"namespace/create/"+$('input[name*=nspace_container]').val(),
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
        var json = $.parseJSON(jqXHR.responseText);
        var n = noty({
            text: json["X-HCP-ErrorMessage"],
            layout: 'top',
            type: 'error'
        });
    }
    });

});

$(".delete-file").click(function (event) {

        event.preventDefault();
        var fileName = $(this).attr("href");
        var postData = {
            name: fileName,
        };

        console.log(postData);

         $.ajax({
            url : BASE_URL+"files/delete/",
            type: "DELETE",
            contentType: "application/json",
            data: JSON.stringify(postData),
            success: function(data, textStatus, jqXHR)
            {
                console.log(textStatus);
                console.log(jqXHR.status);
                var n = noty({
                    text: 'Your file deleted successfully!',
                    layout: 'top',
                    type: 'success'
                });
                function reLoad(){
                    window.location.reload();
                }
                setTimeout(reLoad, 2000);
            },
            error: function (jqXHR, textStatus, errorThrown)
            {
                var json = $.parseJSON(jqXHR.responseText);
                var n = noty({
                    text: textStatus,
                    layout: 'top',
                    type: 'error'
                });
            }

            });

});

$(".create-folder").click(function (event) {

        event.preventDefault();
        var postData = {
            folder_name: "foo",
            namespace_id: 1
        };

         $.ajax({
            url : BASE_URL+"folder/create/",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify(postData),
            success: function(data, textStatus, jqXHR)
            {
                console.log(textStatus);
                console.log(jqXHR.status);
                var n = noty({
                    text: 'Your folder created successfully!',
                    layout: 'top',
                    type: 'success'
                });
                function reLoad(){
                    window.location.reload();
                }
                setTimeout(reLoad, 2000);
            },
            error: function (jqXHR, textStatus, errorThrown)
            {
                var json = $.parseJSON(jqXHR.responseText);
                var n = noty({
                    text: textStatus,
                    layout: 'top',
                    type: 'error'
                });
            }

            });

});