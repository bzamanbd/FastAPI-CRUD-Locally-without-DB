from fastapi import APIRouter
router = APIRouter(tags=["Root"])
root :dict[str,str]= {"Message":"This is the root"}
@router.get("/")
def get_root()-> dict[str,str]:
    return root