from fastapi import APIRouter, Request, Response

from core_common import core_process_request, core_prepare_response, E

router = APIRouter(prefix="/core", tags=["package"])


@router.post("/{gameinfo}/package/list")
async def package_list(request: Request):
    request_info = await core_process_request(request)

    response = E.response(E.package(expire=1200, status=1(url="" name="" desc="" size="" pkgtype="" sumtype="" sum="" from="" till=""))

    response_body, response_headers = await core_prepare_response(request, response)
    return Response(content=response_body, headers=response_headers)


@router.post("/{gameinfo}/package/intend")
async def package_intend(request: Request):
    request_info = await core_process_request(request)

    response = E.response(E.package(status=0))

    response_body, response_headers = await core_prepare_response(request, response)
    return Response(content=response_body, headers=response_headers)
