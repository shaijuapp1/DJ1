function myFunction() {
    alert("t1. Hello from a static file!");
}

var docApp = angular.module("docApp", []);

docApp.controller("docCtrl", function($scope) {

    $scope.init = function(id, title, content){
        $scope.itemId = id
        $scope.title = title
        $scope.content = "content: " + content
    }

    $scope.brnCacel = function() {
        alert(1)

        window.location.href = '/webdoc ';

    };
    $scope.firstName = "John1";
    $scope.lastName = "Doe";

    $scope.Test = function(t1){
        $scope.firstName = "T: " + t1
    }

    $scope.Post = function(){

        var data = {};
        data.id = $scope.itemId
        data.csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val() 
        data.title = $scope.title
        data.content = "Title"

        url = "/webdoc/updateJson"
        //url = "/update/updaterecord/"

        if($scope.itemId){
            url = url + "/" + $scope.itemId 
        }
//url ="/webdoc/updateJson/29"
        $.ajax({
            url : url, //"/webdoc/updateJson/", // "/webdoc/add/addrecord/", // the endpoint
            type : "POST", // http method
            data : data,
            //{ csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val() ,  title : '123', content: '456' }, // data sent with the post request
    
            // handle a successful response
            success : function(json) {
                $('#post-text').val(''); // remove the value from the input
                console.log(json); // log the returned json to the console
                console.log("success"); // another sanity check
            },
    
            // handle a non-successful response
            error : function(xhr,errmsg,err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }

});