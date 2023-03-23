"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import osmosis.gamm.v1beta1.query_pb2

class QueryStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    Pools: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.v1beta1.query_pb2.QueryPoolsRequest,
        osmosis.gamm.v1beta1.query_pb2.QueryPoolsResponse,
    ]
    NumPools: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.v1beta1.query_pb2.QueryNumPoolsRequest,
        osmosis.gamm.v1beta1.query_pb2.QueryNumPoolsResponse,
    ]
    TotalLiquidity: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.v1beta1.query_pb2.QueryTotalLiquidityRequest,
        osmosis.gamm.v1beta1.query_pb2.QueryTotalLiquidityResponse,
    ]
    PoolsWithFilter: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.v1beta1.query_pb2.QueryPoolsWithFilterRequest,
        osmosis.gamm.v1beta1.query_pb2.QueryPoolsWithFilterResponse,
    ]
    """PoolsWithFilter allows you to query specific pools with requested
    parameters
    """
    Pool: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.v1beta1.query_pb2.QueryPoolRequest,
        osmosis.gamm.v1beta1.query_pb2.QueryPoolResponse,
    ]
    """Per Pool gRPC Endpoints"""
    PoolType: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.v1beta1.query_pb2.QueryPoolTypeRequest,
        osmosis.gamm.v1beta1.query_pb2.QueryPoolTypeResponse,
    ]
    """PoolType returns the type of the pool.
    Returns "Balancer" as a string literal when the pool is a balancer pool.
    Errors if the pool is failed to be type caseted.
    """
    CalcJoinPoolNoSwapShares: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.v1beta1.query_pb2.QueryCalcJoinPoolNoSwapSharesRequest,
        osmosis.gamm.v1beta1.query_pb2.QueryCalcJoinPoolNoSwapSharesResponse,
    ]
    """Simulates joining pool without a swap. Returns the amount of shares you'd
    get and tokens needed to provide
    """
    CalcJoinPoolShares: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.v1beta1.query_pb2.QueryCalcJoinPoolSharesRequest,
        osmosis.gamm.v1beta1.query_pb2.QueryCalcJoinPoolSharesResponse,
    ]
    CalcExitPoolCoinsFromShares: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.v1beta1.query_pb2.QueryCalcExitPoolCoinsFromSharesRequest,
        osmosis.gamm.v1beta1.query_pb2.QueryCalcExitPoolCoinsFromSharesResponse,
    ]
    PoolParams: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.v1beta1.query_pb2.QueryPoolParamsRequest,
        osmosis.gamm.v1beta1.query_pb2.QueryPoolParamsResponse,
    ]
    TotalPoolLiquidity: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.v1beta1.query_pb2.QueryTotalPoolLiquidityRequest,
        osmosis.gamm.v1beta1.query_pb2.QueryTotalPoolLiquidityResponse,
    ]
    TotalShares: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.v1beta1.query_pb2.QueryTotalSharesRequest,
        osmosis.gamm.v1beta1.query_pb2.QueryTotalSharesResponse,
    ]
    SpotPrice: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.v1beta1.query_pb2.QuerySpotPriceRequest,
        osmosis.gamm.v1beta1.query_pb2.QuerySpotPriceResponse,
    ]
    """SpotPrice defines a gRPC query handler that returns the spot price given
    a base denomination and a quote denomination.
    """
    EstimateSwapExactAmountIn: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.v1beta1.query_pb2.QuerySwapExactAmountInRequest,
        osmosis.gamm.v1beta1.query_pb2.QuerySwapExactAmountInResponse,
    ]
    """Estimate the swap."""
    EstimateSwapExactAmountOut: grpc.UnaryUnaryMultiCallable[
        osmosis.gamm.v1beta1.query_pb2.QuerySwapExactAmountOutRequest,
        osmosis.gamm.v1beta1.query_pb2.QuerySwapExactAmountOutResponse,
    ]

class QueryServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Pools(
        self,
        request: osmosis.gamm.v1beta1.query_pb2.QueryPoolsRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.v1beta1.query_pb2.QueryPoolsResponse: ...
    @abc.abstractmethod
    def NumPools(
        self,
        request: osmosis.gamm.v1beta1.query_pb2.QueryNumPoolsRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.v1beta1.query_pb2.QueryNumPoolsResponse: ...
    @abc.abstractmethod
    def TotalLiquidity(
        self,
        request: osmosis.gamm.v1beta1.query_pb2.QueryTotalLiquidityRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.v1beta1.query_pb2.QueryTotalLiquidityResponse: ...
    @abc.abstractmethod
    def PoolsWithFilter(
        self,
        request: osmosis.gamm.v1beta1.query_pb2.QueryPoolsWithFilterRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.v1beta1.query_pb2.QueryPoolsWithFilterResponse:
        """PoolsWithFilter allows you to query specific pools with requested
        parameters
        """
    @abc.abstractmethod
    def Pool(
        self,
        request: osmosis.gamm.v1beta1.query_pb2.QueryPoolRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.v1beta1.query_pb2.QueryPoolResponse:
        """Per Pool gRPC Endpoints"""
    @abc.abstractmethod
    def PoolType(
        self,
        request: osmosis.gamm.v1beta1.query_pb2.QueryPoolTypeRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.v1beta1.query_pb2.QueryPoolTypeResponse:
        """PoolType returns the type of the pool.
        Returns "Balancer" as a string literal when the pool is a balancer pool.
        Errors if the pool is failed to be type caseted.
        """
    @abc.abstractmethod
    def CalcJoinPoolNoSwapShares(
        self,
        request: osmosis.gamm.v1beta1.query_pb2.QueryCalcJoinPoolNoSwapSharesRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.v1beta1.query_pb2.QueryCalcJoinPoolNoSwapSharesResponse:
        """Simulates joining pool without a swap. Returns the amount of shares you'd
        get and tokens needed to provide
        """
    @abc.abstractmethod
    def CalcJoinPoolShares(
        self,
        request: osmosis.gamm.v1beta1.query_pb2.QueryCalcJoinPoolSharesRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.v1beta1.query_pb2.QueryCalcJoinPoolSharesResponse: ...
    @abc.abstractmethod
    def CalcExitPoolCoinsFromShares(
        self,
        request: osmosis.gamm.v1beta1.query_pb2.QueryCalcExitPoolCoinsFromSharesRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.v1beta1.query_pb2.QueryCalcExitPoolCoinsFromSharesResponse: ...
    @abc.abstractmethod
    def PoolParams(
        self,
        request: osmosis.gamm.v1beta1.query_pb2.QueryPoolParamsRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.v1beta1.query_pb2.QueryPoolParamsResponse: ...
    @abc.abstractmethod
    def TotalPoolLiquidity(
        self,
        request: osmosis.gamm.v1beta1.query_pb2.QueryTotalPoolLiquidityRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.v1beta1.query_pb2.QueryTotalPoolLiquidityResponse: ...
    @abc.abstractmethod
    def TotalShares(
        self,
        request: osmosis.gamm.v1beta1.query_pb2.QueryTotalSharesRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.v1beta1.query_pb2.QueryTotalSharesResponse: ...
    @abc.abstractmethod
    def SpotPrice(
        self,
        request: osmosis.gamm.v1beta1.query_pb2.QuerySpotPriceRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.v1beta1.query_pb2.QuerySpotPriceResponse:
        """SpotPrice defines a gRPC query handler that returns the spot price given
        a base denomination and a quote denomination.
        """
    @abc.abstractmethod
    def EstimateSwapExactAmountIn(
        self,
        request: osmosis.gamm.v1beta1.query_pb2.QuerySwapExactAmountInRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.v1beta1.query_pb2.QuerySwapExactAmountInResponse:
        """Estimate the swap."""
    @abc.abstractmethod
    def EstimateSwapExactAmountOut(
        self,
        request: osmosis.gamm.v1beta1.query_pb2.QuerySwapExactAmountOutRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.gamm.v1beta1.query_pb2.QuerySwapExactAmountOutResponse: ...

def add_QueryServicer_to_server(servicer: QueryServicer, server: grpc.Server) -> None: ...