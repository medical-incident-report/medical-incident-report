//
// This is the main PatientSummary class for OPAL.
//
angular.module('opal.services').factory('PatientSummary', function(UserProfile) {
        var PatientSummary = function(jsonResponse){
            _.extend(this, jsonResponse);
            this.link = "/#/patient/" + jsonResponse.patient_id;
        };

        return PatientSummary;
    });
