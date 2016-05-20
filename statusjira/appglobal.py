#!/usr/bin/python3

class status (object):
    """Contains status onstants used by the statusjira package"""

    #Valid ticket status values

    _unknown = -1            #Status value is not available
    _open = 1                #Verified in Jira
    _developerTest = 10006   #Verified in Jira   
    _inProgress = 3          #Verified in Jira
    _resolved = 5            #Verified in Jira
    _reopened = 4            #Verified in Jira   
    _closed = 6              #Verified in Jira
    _productBacklog = 991    # -- Not Verified --
    _codeReview = 10004      #Verified in Jira
    _approved = 10015        #Verified in Jira
    _waitingForInput = 10822 #Verified in Jira
    _pendingApproval = 10021 #Verified in Jira

    # List used to determine if a given status value is valid
    _valid = [_unknown, _open, _developerTest, _inProgress, _resolved, 
              _reopened, _closed, _productBacklog, _codeReview, 
              _approved, _waitingForInput, _pendingApproval]

    #Percent complete values that correspond to each status value above
    _pctOpen = 0
    _pctDeveloperTest = 50
    _pctInProgress = 25
    _pctResolved = 75
    _pctReopened = 0
    _pctClosed = 100
    _pctProductBacklog = 0
    _pctCodeReview = 50
    _pctApproved = 100
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
                        _approved:_pctApproved,
                        _waitingForInput:_pctWaitingForInput, 
                        _pendingApproval:_pctPendingApproval}

    #Dictionary used to convert status ID's into their corresponding status values
    _text = {_unknown:'unknown', _open:'Open', _developerTest:'Developer Test',
             _inProgress:'In Progress', _resolved:'Resolved', _reopened:'Re-Opened', 
             _closed:'Closed', _productBacklog:'Product Backlog', _codeReview:'Code Review',
             _approved:'Approved', _waitingForInput:'Waiting For Input', _pendingApproval:'PendingApproval'}

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

class type (object):
    """Contains ticket type constants"""

    #Ticket type ID's
    _unknown = -1
    _bug = 1
    _sccbreq = 10000
    _archdesign = 10202
    _analysis = 22
    _task = 3
    _subtask = 5
    _epic = 6
    _story = 7

    #Mapping of ticket type ID's to ticket type names
    _name = {_unknown:'Unknown',
            _bug:'Bug',
            _sccbreq:'SCCB Request',
            _archdesign:'Architecture Design',
            _analysis:'Analysis',
            _task:'Task',
            _subtask:'Sub-Task',
            _epic:'Epic',
            _story:'Story'}




