"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import cosmos.base.v1beta1.coin_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Params(google.protobuf.message.Message):
    """Params defines the set of params for the distribution module."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMMUNITY_TAX_FIELD_NUMBER: builtins.int
    BASE_PROPOSER_REWARD_FIELD_NUMBER: builtins.int
    BONUS_PROPOSER_REWARD_FIELD_NUMBER: builtins.int
    WITHDRAW_ADDR_ENABLED_FIELD_NUMBER: builtins.int
    community_tax: builtins.str
    base_proposer_reward: builtins.str
    bonus_proposer_reward: builtins.str
    withdraw_addr_enabled: builtins.bool
    def __init__(
        self,
        *,
        community_tax: builtins.str = ...,
        base_proposer_reward: builtins.str = ...,
        bonus_proposer_reward: builtins.str = ...,
        withdraw_addr_enabled: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["base_proposer_reward", b"base_proposer_reward", "bonus_proposer_reward", b"bonus_proposer_reward", "community_tax", b"community_tax", "withdraw_addr_enabled", b"withdraw_addr_enabled"]) -> None: ...

global___Params = Params

@typing_extensions.final
class ValidatorHistoricalRewards(google.protobuf.message.Message):
    """ValidatorHistoricalRewards represents historical rewards for a validator.
    Height is implicit within the store key.
    Cumulative reward ratio is the sum from the zeroeth period
    until this period of rewards / tokens, per the spec.
    The reference count indicates the number of objects
    which might need to reference this historical entry at any point.
    ReferenceCount =
       number of outstanding delegations which ended the associated period (and
       might need to read that record)
     + number of slashes which ended the associated period (and might need to
     read that record)
     + one per validator for the zeroeth period, set on initialization
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CUMULATIVE_REWARD_RATIO_FIELD_NUMBER: builtins.int
    REFERENCE_COUNT_FIELD_NUMBER: builtins.int
    @property
    def cumulative_reward_ratio(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.DecCoin]: ...
    reference_count: builtins.int
    def __init__(
        self,
        *,
        cumulative_reward_ratio: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.DecCoin] | None = ...,
        reference_count: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["cumulative_reward_ratio", b"cumulative_reward_ratio", "reference_count", b"reference_count"]) -> None: ...

global___ValidatorHistoricalRewards = ValidatorHistoricalRewards

@typing_extensions.final
class ValidatorCurrentRewards(google.protobuf.message.Message):
    """ValidatorCurrentRewards represents current rewards and current
    period for a validator kept as a running counter and incremented
    each block as long as the validator's tokens remain constant.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REWARDS_FIELD_NUMBER: builtins.int
    PERIOD_FIELD_NUMBER: builtins.int
    @property
    def rewards(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.DecCoin]: ...
    period: builtins.int
    def __init__(
        self,
        *,
        rewards: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.DecCoin] | None = ...,
        period: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["period", b"period", "rewards", b"rewards"]) -> None: ...

global___ValidatorCurrentRewards = ValidatorCurrentRewards

@typing_extensions.final
class ValidatorAccumulatedCommission(google.protobuf.message.Message):
    """ValidatorAccumulatedCommission represents accumulated commission
    for a validator kept as a running counter, can be withdrawn at any time.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMMISSION_FIELD_NUMBER: builtins.int
    @property
    def commission(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.DecCoin]: ...
    def __init__(
        self,
        *,
        commission: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.DecCoin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["commission", b"commission"]) -> None: ...

global___ValidatorAccumulatedCommission = ValidatorAccumulatedCommission

@typing_extensions.final
class ValidatorOutstandingRewards(google.protobuf.message.Message):
    """ValidatorOutstandingRewards represents outstanding (un-withdrawn) rewards
    for a validator inexpensive to track, allows simple sanity checks.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REWARDS_FIELD_NUMBER: builtins.int
    @property
    def rewards(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.DecCoin]: ...
    def __init__(
        self,
        *,
        rewards: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.DecCoin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["rewards", b"rewards"]) -> None: ...

global___ValidatorOutstandingRewards = ValidatorOutstandingRewards

@typing_extensions.final
class ValidatorSlashEvent(google.protobuf.message.Message):
    """ValidatorSlashEvent represents a validator slash event.
    Height is implicit within the store key.
    This is needed to calculate appropriate amount of staking tokens
    for delegations which are withdrawn after a slash has occurred.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALIDATOR_PERIOD_FIELD_NUMBER: builtins.int
    FRACTION_FIELD_NUMBER: builtins.int
    validator_period: builtins.int
    fraction: builtins.str
    def __init__(
        self,
        *,
        validator_period: builtins.int = ...,
        fraction: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["fraction", b"fraction", "validator_period", b"validator_period"]) -> None: ...

global___ValidatorSlashEvent = ValidatorSlashEvent

@typing_extensions.final
class ValidatorSlashEvents(google.protobuf.message.Message):
    """ValidatorSlashEvents is a collection of ValidatorSlashEvent messages."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALIDATOR_SLASH_EVENTS_FIELD_NUMBER: builtins.int
    @property
    def validator_slash_events(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ValidatorSlashEvent]: ...
    def __init__(
        self,
        *,
        validator_slash_events: collections.abc.Iterable[global___ValidatorSlashEvent] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["validator_slash_events", b"validator_slash_events"]) -> None: ...

global___ValidatorSlashEvents = ValidatorSlashEvents

@typing_extensions.final
class FeePool(google.protobuf.message.Message):
    """FeePool is the global fee pool for distribution."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMMUNITY_POOL_FIELD_NUMBER: builtins.int
    @property
    def community_pool(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.DecCoin]: ...
    def __init__(
        self,
        *,
        community_pool: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.DecCoin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["community_pool", b"community_pool"]) -> None: ...

global___FeePool = FeePool

@typing_extensions.final
class CommunityPoolSpendProposal(google.protobuf.message.Message):
    """CommunityPoolSpendProposal details a proposal for use of community funds,
    together with how many coins are proposed to be spent, and to which
    recipient account.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TITLE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    RECIPIENT_FIELD_NUMBER: builtins.int
    AMOUNT_FIELD_NUMBER: builtins.int
    title: builtins.str
    description: builtins.str
    recipient: builtins.str
    @property
    def amount(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.Coin]: ...
    def __init__(
        self,
        *,
        title: builtins.str = ...,
        description: builtins.str = ...,
        recipient: builtins.str = ...,
        amount: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.Coin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["amount", b"amount", "description", b"description", "recipient", b"recipient", "title", b"title"]) -> None: ...

global___CommunityPoolSpendProposal = CommunityPoolSpendProposal

@typing_extensions.final
class DelegatorStartingInfo(google.protobuf.message.Message):
    """DelegatorStartingInfo represents the starting info for a delegator reward
    period. It tracks the previous validator period, the delegation's amount of
    staking token, and the creation height (to check later on if any slashes have
    occurred). NOTE: Even though validators are slashed to whole staking tokens,
    the delegators within the validator may be left with less than a full token,
    thus sdk.Dec is used.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PREVIOUS_PERIOD_FIELD_NUMBER: builtins.int
    STAKE_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    previous_period: builtins.int
    stake: builtins.str
    height: builtins.int
    def __init__(
        self,
        *,
        previous_period: builtins.int = ...,
        stake: builtins.str = ...,
        height: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["height", b"height", "previous_period", b"previous_period", "stake", b"stake"]) -> None: ...

global___DelegatorStartingInfo = DelegatorStartingInfo

@typing_extensions.final
class DelegationDelegatorReward(google.protobuf.message.Message):
    """DelegationDelegatorReward represents the properties
    of a delegator's delegation reward.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VALIDATOR_ADDRESS_FIELD_NUMBER: builtins.int
    REWARD_FIELD_NUMBER: builtins.int
    validator_address: builtins.str
    @property
    def reward(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[cosmos.base.v1beta1.coin_pb2.DecCoin]: ...
    def __init__(
        self,
        *,
        validator_address: builtins.str = ...,
        reward: collections.abc.Iterable[cosmos.base.v1beta1.coin_pb2.DecCoin] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["reward", b"reward", "validator_address", b"validator_address"]) -> None: ...

global___DelegationDelegatorReward = DelegationDelegatorReward

@typing_extensions.final
class CommunityPoolSpendProposalWithDeposit(google.protobuf.message.Message):
    """CommunityPoolSpendProposalWithDeposit defines a CommunityPoolSpendProposal
    with a deposit
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TITLE_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    RECIPIENT_FIELD_NUMBER: builtins.int
    AMOUNT_FIELD_NUMBER: builtins.int
    DEPOSIT_FIELD_NUMBER: builtins.int
    title: builtins.str
    description: builtins.str
    recipient: builtins.str
    amount: builtins.str
    deposit: builtins.str
    def __init__(
        self,
        *,
        title: builtins.str = ...,
        description: builtins.str = ...,
        recipient: builtins.str = ...,
        amount: builtins.str = ...,
        deposit: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["amount", b"amount", "deposit", b"deposit", "description", b"description", "recipient", b"recipient", "title", b"title"]) -> None: ...

global___CommunityPoolSpendProposalWithDeposit = CommunityPoolSpendProposalWithDeposit