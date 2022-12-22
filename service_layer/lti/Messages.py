class JWTMessage():
    typ = None # REQUIRED (JWT)
    alg = None # REQUIRED (RS256)
    kid = None # REQUIRED (key id)
    iss = None # REQUIRES (issuer)
    aud = None # REQUIRED (audience)
    sub = None # REQUIRED subject identifier  It MUST NOT exceed 255 ASCII characters in length
    exp = None # REQUIRED (expiration time)
    iat = None # REQUIRED (issued at)
    nonce = None # REQUIRED (nonce)
    azp = None # OPTIONAL (authorized party) if multiple audiences are present

class LTIContext():
    id = None # REQUIRED (context id)
    label = None # OPTIONAL (context label)
    title = None # OPTIONAL (context title)
    type : list[str] # OPTIONAL (context type: potential array)

class LTIExtension():
    user_username = None # OPTIONAL (user username)
    lms = None # OPTIONAL (lms e.g. Moodle Name)

class LTILIS():
    person_name_given = None # OPTIONAL (person name given)
    person_name_family = None # OPTIONAL (person name family)
    person_name_full = None # OPTIONAL (person name full)
    person_contact_email_primary = None # OPTIONAL (person contact email primary)
    person_sourcedid = None # OPTIONAL (person sourcedid)
    course_section_sourcedid = None # OPTIONAL (course section sourcedid)

# todo validate
class LTIResourceLink():
    id = None # REQUIRED (resource link id)
    title = None # OPTIONAL (resource link title)
    description = None # OPTIONAL (resource link description)

class LTILISResultSourcedIdData():
    instanceid = None # REQUIRED (instance id)
    userid = None # REQUIRED (user id)
    typeid = None # REQUIRED (type id)
    launchid = None # REQUIRED (launch id)
    hash = None # REQUIRED (hash)

class LTILISResultSourcedId():
    data : LTILISResultSourcedIdData

class LTIBasicOutcome():
    lis_result_sourcedid : LTILISResultSourcedId # REQUIRED (lis result sourcedid)
    lis_outcome_service_url = None # REQUIRED (lis outcome service url)

class LTILaunchPresentation():
    document_target = None # OPTIONAL (document target)
    height = None # OPTIONAL (height)
    width = None # OPTIONAL (width)
    return_url = None # OPTIONAL (return url)
    locale = None # OPTIONAL (locale)
    css_url = None # OPTIONAL (css url)

class LTIToolPlatform():
    guid = None # OPTIONAL (guid)
    name = None # OPTIONAL (name: site name)
    version = None # OPTIONAL (version: e.g. "2022112800")
    product_family_code = None # OPTIONAL (product family code:e.g. "moodle")
    description = None # OPTIONAL (description)
    url = None # OPTIONAL (url)

class LTIIDToken(JWTMessage):
    """
    https://www.imsglobal.org/spec/security/v1p0/#id-token 
    https://www.imsglobal.org/spec/security/v1p0/#authentication-response-validation
    """
    deployment_id = None # REQUIRED (deployment id)
    target_link_uri = None # REQUIRED (target link uri)
    lis : LTILIS # OPTIONAL (LIS) Learning Information Services
    roles = None # OPTIONAL (roles)
    context : LTIContext # OPTIONAL (context)
    message_type = None # REQUIRED (message type)
    resource_link : LTIResourceLink # OPTIONAL (resource link)
    basicoutcome = None # OPTIONAL (basic outcome)
    given_name = None # OPTIONAL (given name)
    family_name = None # OPTIONAL (family name)
    email = None # OPTIONAL (email)
    name = None # OPTIONAL (name)
    ext : LTIExtension # OPTIONAL (extensions)
    launch_presentation : LTILaunchPresentation # OPTIONAL (launch presentation)
    tool_platform : LTIToolPlatform # OPTIONAL (tool platform)
    version = None # OPTIONAL (version)