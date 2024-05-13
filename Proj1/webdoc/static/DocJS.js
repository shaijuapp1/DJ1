function myFunction() {
    alert("t1. Hello from a static file!");
}

var docApp = angular.module("docApp", []);

docApp.controller("docCtrl", function($scope) {

    $scope.brnCacel = function() {
        window.location.href = '/webdoc ';

    };
  $scope.firstName = "John";
  $scope.lastName = "Doe";



});