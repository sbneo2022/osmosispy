"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import grpc
import osmosis.superfluid.query_pb2

class QueryStub:
    """Query defines the gRPC querier service."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    Params: grpc.UnaryUnaryMultiCallable[
        osmosis.superfluid.query_pb2.QueryParamsRequest,
        osmosis.superfluid.query_pb2.QueryParamsResponse,
    ]
    """Params returns the total set of superfluid parameters."""
    AssetType: grpc.UnaryUnaryMultiCallable[
        osmosis.superfluid.query_pb2.AssetTypeRequest,
        osmosis.superfluid.query_pb2.AssetTypeResponse,
    ]
    """Returns superfluid asset type, whether if it's a native asset or an lp
    share.
    """
    AllAssets: grpc.UnaryUnaryMultiCallable[
        osmosis.superfluid.query_pb2.AllAssetsRequest,
        osmosis.superfluid.query_pb2.AllAssetsResponse,
    ]
    """Returns all registered superfluid assets."""
    AssetMultiplier: grpc.UnaryUnaryMultiCallable[
        osmosis.superfluid.query_pb2.AssetMultiplierRequest,
        osmosis.superfluid.query_pb2.AssetMultiplierResponse,
    ]
    """Returns the osmo equivalent multiplier used in the most recent epoch."""
    AllIntermediaryAccounts: grpc.UnaryUnaryMultiCallable[
        osmosis.superfluid.query_pb2.AllIntermediaryAccountsRequest,
        osmosis.superfluid.query_pb2.AllIntermediaryAccountsResponse,
    ]
    """Returns all superfluid intermediary accounts."""
    ConnectedIntermediaryAccount: grpc.UnaryUnaryMultiCallable[
        osmosis.superfluid.query_pb2.ConnectedIntermediaryAccountRequest,
        osmosis.superfluid.query_pb2.ConnectedIntermediaryAccountResponse,
    ]
    """Returns intermediary account connected to a superfluid staked lock by id"""
    TotalDelegationByValidatorForDenom: grpc.UnaryUnaryMultiCallable[
        osmosis.superfluid.query_pb2.QueryTotalDelegationByValidatorForDenomRequest,
        osmosis.superfluid.query_pb2.QueryTotalDelegationByValidatorForDenomResponse,
    ]
    """Returns the amount of delegations of specific denom for all validators"""
    TotalSuperfluidDelegations: grpc.UnaryUnaryMultiCallable[
        osmosis.superfluid.query_pb2.TotalSuperfluidDelegationsRequest,
        osmosis.superfluid.query_pb2.TotalSuperfluidDelegationsResponse,
    ]
    """Returns the total amount of osmo superfluidly staked.
    Response is denominated in uosmo.
    """
    SuperfluidDelegationAmount: grpc.UnaryUnaryMultiCallable[
        osmosis.superfluid.query_pb2.SuperfluidDelegationAmountRequest,
        osmosis.superfluid.query_pb2.SuperfluidDelegationAmountResponse,
    ]
    """Returns the coins superfluid delegated for the delegator, validator, denom
    triplet
    """
    SuperfluidDelegationsByDelegator: grpc.UnaryUnaryMultiCallable[
        osmosis.superfluid.query_pb2.SuperfluidDelegationsByDelegatorRequest,
        osmosis.superfluid.query_pb2.SuperfluidDelegationsByDelegatorResponse,
    ]
    """Returns all the delegated superfluid poistions for a specific delegator."""
    SuperfluidUndelegationsByDelegator: grpc.UnaryUnaryMultiCallable[
        osmosis.superfluid.query_pb2.SuperfluidUndelegationsByDelegatorRequest,
        osmosis.superfluid.query_pb2.SuperfluidUndelegationsByDelegatorResponse,
    ]
    """Returns all the undelegating superfluid poistions for a specific delegator."""
    SuperfluidDelegationsByValidatorDenom: grpc.UnaryUnaryMultiCallable[
        osmosis.superfluid.query_pb2.SuperfluidDelegationsByValidatorDenomRequest,
        osmosis.superfluid.query_pb2.SuperfluidDelegationsByValidatorDenomResponse,
    ]
    """Returns all the superfluid positions of a specific denom delegated to one
    validator
    """
    EstimateSuperfluidDelegatedAmountByValidatorDenom: grpc.UnaryUnaryMultiCallable[
        osmosis.superfluid.query_pb2.EstimateSuperfluidDelegatedAmountByValidatorDenomRequest,
        osmosis.superfluid.query_pb2.EstimateSuperfluidDelegatedAmountByValidatorDenomResponse,
    ]
    """Returns the amount of a specific denom delegated to a specific validator
    This is labeled an estimate, because the way it calculates the amount can
    lead rounding errors from the true delegated amount
    """
    TotalDelegationByDelegator: grpc.UnaryUnaryMultiCallable[
        osmosis.superfluid.query_pb2.QueryTotalDelegationByDelegatorRequest,
        osmosis.superfluid.query_pb2.QueryTotalDelegationByDelegatorResponse,
    ]
    """Returns the specified delegations for a specific delegator"""
    UnpoolWhitelist: grpc.UnaryUnaryMultiCallable[
        osmosis.superfluid.query_pb2.QueryUnpoolWhitelistRequest,
        osmosis.superfluid.query_pb2.QueryUnpoolWhitelistResponse,
    ]
    """Returns a list of whitelisted pool ids to unpool."""

class QueryServicer(metaclass=abc.ABCMeta):
    """Query defines the gRPC querier service."""

    @abc.abstractmethod
    def Params(
        self,
        request: osmosis.superfluid.query_pb2.QueryParamsRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.superfluid.query_pb2.QueryParamsResponse:
        """Params returns the total set of superfluid parameters."""
    @abc.abstractmethod
    def AssetType(
        self,
        request: osmosis.superfluid.query_pb2.AssetTypeRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.superfluid.query_pb2.AssetTypeResponse:
        """Returns superfluid asset type, whether if it's a native asset or an lp
        share.
        """
    @abc.abstractmethod
    def AllAssets(
        self,
        request: osmosis.superfluid.query_pb2.AllAssetsRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.superfluid.query_pb2.AllAssetsResponse:
        """Returns all registered superfluid assets."""
    @abc.abstractmethod
    def AssetMultiplier(
        self,
        request: osmosis.superfluid.query_pb2.AssetMultiplierRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.superfluid.query_pb2.AssetMultiplierResponse:
        """Returns the osmo equivalent multiplier used in the most recent epoch."""
    @abc.abstractmethod
    def AllIntermediaryAccounts(
        self,
        request: osmosis.superfluid.query_pb2.AllIntermediaryAccountsRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.superfluid.query_pb2.AllIntermediaryAccountsResponse:
        """Returns all superfluid intermediary accounts."""
    @abc.abstractmethod
    def ConnectedIntermediaryAccount(
        self,
        request: osmosis.superfluid.query_pb2.ConnectedIntermediaryAccountRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.superfluid.query_pb2.ConnectedIntermediaryAccountResponse:
        """Returns intermediary account connected to a superfluid staked lock by id"""
    @abc.abstractmethod
    def TotalDelegationByValidatorForDenom(
        self,
        request: osmosis.superfluid.query_pb2.QueryTotalDelegationByValidatorForDenomRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.superfluid.query_pb2.QueryTotalDelegationByValidatorForDenomResponse:
        """Returns the amount of delegations of specific denom for all validators"""
    @abc.abstractmethod
    def TotalSuperfluidDelegations(
        self,
        request: osmosis.superfluid.query_pb2.TotalSuperfluidDelegationsRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.superfluid.query_pb2.TotalSuperfluidDelegationsResponse:
        """Returns the total amount of osmo superfluidly staked.
        Response is denominated in uosmo.
        """
    @abc.abstractmethod
    def SuperfluidDelegationAmount(
        self,
        request: osmosis.superfluid.query_pb2.SuperfluidDelegationAmountRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.superfluid.query_pb2.SuperfluidDelegationAmountResponse:
        """Returns the coins superfluid delegated for the delegator, validator, denom
        triplet
        """
    @abc.abstractmethod
    def SuperfluidDelegationsByDelegator(
        self,
        request: osmosis.superfluid.query_pb2.SuperfluidDelegationsByDelegatorRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.superfluid.query_pb2.SuperfluidDelegationsByDelegatorResponse:
        """Returns all the delegated superfluid poistions for a specific delegator."""
    @abc.abstractmethod
    def SuperfluidUndelegationsByDelegator(
        self,
        request: osmosis.superfluid.query_pb2.SuperfluidUndelegationsByDelegatorRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.superfluid.query_pb2.SuperfluidUndelegationsByDelegatorResponse:
        """Returns all the undelegating superfluid poistions for a specific delegator."""
    @abc.abstractmethod
    def SuperfluidDelegationsByValidatorDenom(
        self,
        request: osmosis.superfluid.query_pb2.SuperfluidDelegationsByValidatorDenomRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.superfluid.query_pb2.SuperfluidDelegationsByValidatorDenomResponse:
        """Returns all the superfluid positions of a specific denom delegated to one
        validator
        """
    @abc.abstractmethod
    def EstimateSuperfluidDelegatedAmountByValidatorDenom(
        self,
        request: osmosis.superfluid.query_pb2.EstimateSuperfluidDelegatedAmountByValidatorDenomRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.superfluid.query_pb2.EstimateSuperfluidDelegatedAmountByValidatorDenomResponse:
        """Returns the amount of a specific denom delegated to a specific validator
        This is labeled an estimate, because the way it calculates the amount can
        lead rounding errors from the true delegated amount
        """
    @abc.abstractmethod
    def TotalDelegationByDelegator(
        self,
        request: osmosis.superfluid.query_pb2.QueryTotalDelegationByDelegatorRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.superfluid.query_pb2.QueryTotalDelegationByDelegatorResponse:
        """Returns the specified delegations for a specific delegator"""
    @abc.abstractmethod
    def UnpoolWhitelist(
        self,
        request: osmosis.superfluid.query_pb2.QueryUnpoolWhitelistRequest,
        context: grpc.ServicerContext,
    ) -> osmosis.superfluid.query_pb2.QueryUnpoolWhitelistResponse:
        """Returns a list of whitelisted pool ids to unpool."""

def add_QueryServicer_to_server(servicer: QueryServicer, server: grpc.Server) -> None: ...
