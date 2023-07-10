class JWTMessage:
    typ = None  # REQUIRED (JWT)
    alg = None  # REQUIRED (RS256)
    kid = None  # REQUIRED (key id)
    iss = None  # REQUIRES (issuer)
    aud = None  # REQUIRED (audience)
    sub = None  # REQUIRED subject identifier  It MUST NOT exceed 255 ASCII characters in length
    exp = None  # REQUIRED (expiration time)
    iat = None  # REQUIRED (issued at)
    nonce = None  # REQUIRED (nonce)
    azp = None  # OPTIONAL (authorized party) if multiple audiences are present

    def __init__(self) -> None:
        """Check if all member variables are set"""
        for key in self.__dict__:
            if key == "azp":
                continue
            if self.__dict__[key] is None:
                raise ValueError(f"JWTMessage: {key} is not set")


class LTIContext:
    id = None  # REQUIRED (context id)
    label = None  # OPTIONAL (context label)
    title = None  # OPTIONAL (context title)
    type: list[str]  # OPTIONAL (context type: potential array)


class LTIExtension:
    user_username = None  # OPTIONAL (user username)
    lms = None  # OPTIONAL (lms e.g. Moodle Name)


class LTILIS:
    person_name_given = None  # OPTIONAL (person name given)
    person_name_family = None  # OPTIONAL (person name family)
    person_name_full = None  # OPTIONAL (person name full)
    # OPTIONAL (person contact email primary)
    person_contact_email_primary = None
    person_sourcedid = None  # OPTIONAL (person sourcedid)
    course_section_sourcedid = None  # OPTIONAL (course section sourcedid)


class LTIResourceLink:
    id = None  # REQUIRED (resource link id)
    title = None  # OPTIONAL (resource link title)
    description = None  # OPTIONAL (resource link description)


class LTILISResultSourcedIdData:
    instanceid = None  # REQUIRED (instance id)
    userid = None  # REQUIRED (user id)
    typeid = None  # REQUIRED (type id)
    launchid = None  # REQUIRED (launch id)
    hash = None  # REQUIRED (hash)


class LTILISResultSourcedId:
    data: LTILISResultSourcedIdData


class LTIBasicOutcome:
    # REQUIRED (lis result sourcedid)
    lis_result_sourcedid: LTILISResultSourcedId
    lis_outcome_service_url = None  # REQUIRED (lis outcome service url)


class LTILaunchPresentation:
    document_target = None  # OPTIONAL (document target)
    height = None  # OPTIONAL (height)
    width = None  # OPTIONAL (width)
    return_url = None  # OPTIONAL (return url)
    locale = None  # OPTIONAL (locale)
    css_url = None  # OPTIONAL (css url)


class LTIToolPlatform:
    guid = None  # OPTIONAL (guid)
    name = None  # OPTIONAL (name: site name)
    version = None  # OPTIONAL (version: e.g. "2022112800")
    product_family_code = None  # OPTIONAL (product family code:e.g. "moodle")
    description = None  # OPTIONAL (description)
    url = None  # OPTIONAL (url)


class LTIIDToken(JWTMessage):
    """
    Holds the ID Token from the LTI 1.3 OIDC Authentication Response. The token contains LTI claims and is signed by the LMS.
    https://www.imsglobal.org/spec/security/v1p0/#id-token
    https://www.imsglobal.org/spec/security/v1p0/#authentication-response-validation
    """

    deployment_id = None  # REQUIRED (deployment id)
    target_link_uri = None  # REQUIRED (target link uri)
    lis: LTILIS  # OPTIONAL (LIS) Learning Information Services
    roles = None  # OPTIONAL (roles)
    context: LTIContext  # OPTIONAL (context)
    message_type = None  # REQUIRED (message type)
    resource_link: LTIResourceLink  # OPTIONAL (resource link)
    basicoutcome = None  # OPTIONAL (basic outcome)
    given_name = None  # OPTIONAL (given name)
    family_name = None  # OPTIONAL (family name)
    email = None  # OPTIONAL (email)
    name = None  # OPTIONAL (full name)
    ext: LTIExtension  # OPTIONAL (extensions)
    # OPTIONAL (launch presentation)
    launch_presentation: LTILaunchPresentation
    tool_platform: LTIToolPlatform  # OPTIONAL (tool platform)
    version = None  # OPTIONAL (version)
    nonce: str  # REQUIRED (nonce)

    def __init__(self, **entries):
        """Check if all member variables are set"""
        self.__dict__.update(entries)
        super().__init__()

        for key in self.__dict__:
            if (
                key == "deployment_id"
                or key == "target_link_uri"
                or key == "message_type"
                or key == "nonce"
            ):
                if self.__dict__[key] is None:
                    raise ValueError(f"LTIIDToken: {key} is not set")
            else:
                continue

    def __getitem__(self, key):
        return self.__dict__[key]
