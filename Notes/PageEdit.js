var app = angular.module("myApp", []);
app.controller("myCtrl", function($scope) {
    
    $scope.ls = [];
    $scope.NewPos = [];
    $scope.edit = {};

    $scope.source = [];

   // Not ot close model on escape
    $('#editModal').modal({
        backdrop: 'static',
        keyboard: false
    })

    //$scope.NewPos = Position.length + 1;

    $scope.brnAdd = function() {
        $scope.AddNew = true;
        $scope.NewColums = "1"  
        $scope.NewType = "h1"  
        $scope.edit = {}
        $scope.UpdatePosList()
        $('#editModal').modal('show');
    }

    $scope.btnSave = function() {
        if($scope.AddNew ){
            $scope.source.push($scope.edit)
        }
        $('#editModal').modal('hide');
    }

    $scope.btnCose = function() {
debugger
        $.confirm({
            title: 'Confirm!',
            content: 'Simple close!',
            buttons: {
                Close: function () {
                    $('#editModal').modal('hide');
                },
                cancel: function () {
                    //$.alert('Canceled!');
                }
            }
        });
    }

    $scope.UpdateStyle = function() {
        if($scope.edit.cl){
            for(i=0;i<$scope.edit.cl.length;i++){
                $scope.edit.cl[i].s = $scope.NewType
            }
        }
    }

    $scope.UpdatePosList = function() {
debugger
        var start = 0;
        var end = $scope.NewColums

        if( $scope.edit.cl  ){
            if($scope.edit.cl.length > $scope.NewColums){
                $scope.edit.cl.splice($scope.NewColums)
                end = 0
            }
            else if($scope.edit.cl.length < $scope.NewColums) {
                start = $scope.edit.cl.length
            }
        }
        else{
            $scope.edit = {}
            $scope.edit.cl = []
        }

        for(i=start;i<end;i++){
            var c = {}
            var val = i+1
            c.val = "-" + val  + "-"
            c.s = $scope.NewType
            $scope.edit.cl.push(c)
        }

        $scope.edit.colCls = "col-sm-" + 12/$scope.NewColums
    }

});

