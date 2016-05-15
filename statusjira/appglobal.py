#!/usr/bin/python3

class status (object):
    """Contains status onstants used by the statusjira package"""

    #Valid ticket status values

    _unknown = -1            #Status value is not available
    _open = 1                #Verified in Jira
    _developerTest = 10006   #Verified in Jira   
    _inProgress = 3          #Verified in Jira
    _resolved = 5            #Verified in Jira
    _reopened = 992          # -- Not Verified --
    _closed = 6              #Verified in Jira
    _productBacklog = 991    # -- Not Verified --
    _codeReview = 10004      #Verified in Jira
    _waitingForInput = 10822 #Verified in Jira
    _pendingApproval = 10021 #Verified in Jira

    # List used to determine if a given status value is valid
    _valid = [_unknown, _open, _developerTest, _inProgress, _resolved, 
              _reopened, _closed, _productBacklog, _codeReview, 
              _waitingForInput, _pendingApproval]

    #Percent complete values that correspond to each status value above
    _pctOpen = 0
    _pctDeveloperTest = 50
    _pctInProgress = 25
    _pctResolved = 75
    _pctReopened = 0
    _pctClosed = 100
    _pctProductBacklog = 0
    _pctCodeReview = 50
    _pctWaitingForInput = 0
    _pctPendingApproval = 0
    
    #Dictionary used to convert a valid status value to its corresponding percent
    #percent complete value.

    _percentcomplete = {_open:_pctOpen,
                        _developerTest:_pctDeveloperTest,
                        _inProgress:_pctInProgress, 
                        _resolved:_pctResolved,
                        _reopened:_pctReopened, 
                        _closed:_pctClosed,
                        _productBacklog:_pctProductBacklog, 
                        _codeReview:_pctCodeReview,
                        _waitingForInput:_pctWaitingForInput, 
                        _pendingApproval:_pctPendingApproval}

class tags (object):
    """Contains tag constants used by the status jira package"""

    #Following are tag names that are referenced in the applicaton

    #Tag names used to extract duration data    
    _secondsplanned="timeoriginalestimate"
    _secondsworked="timespent"
    _secondsremain="timeestimate"

    #Tag information to extract custom data
    _customfield="customfield"                              #Tag name
    _customfieldname="customfieldname"                      #Tag name
    _customfieldvalue="customfieldvalues/customfieldvalue"  #Tag name
    _epiclink="Epic Link"                                   #Tag value

