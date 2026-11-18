#!/usr/bin/env python3
"""Guard the corrected Crypto Trend Rider's key safety/accounting invariants.

This is a source-level regression check, not a Pine compiler or backtest.
TradingView compilation and realistic exchange-specific testing remain external.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / "Crypto_Trend_Rider_4H.pine").read_text(encoding="utf-8")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"Pine static validation failed: {message}")


require(source.startswith("//@version=5"), "expected Pine v5 source")
require('indicator("Crypto Trend Rider' in source, "script must remain explicitly labelled as an indicator simulation")
require("strategy(" not in source, "do not imply Strategy Tester execution")
require("barstate.isconfirmed and not wasInTrade and emaCrossUp" in source, "first entry must be confirmed-bar only")
require("barstate.isconfirmed and enablePyramidOnPullback" in source, "add entry must be confirmed-bar only")
require("barstate.isconfirmed and wasInTrade and not na(stopForBar) and low <= stopForBar" in source, "initial/trailing stop must be enforced on a confirmed bar")
require("math.max(chandelierLine[1], chandelierCandidate)" in source, "long Chandelier stop must ratchet and use prior stop")
require("barstate.isconfirmed and wasInTrade and (trendBreakExit or stopHit)" in source, "full exits must be confirmed-bar only")
require("high >= targetP" in source, "partial target must use an intrabar high touch")
require("bar_index > array.get(legEntryBar, i)" in source, "new entries must not be partially exited on their entry bar")
require("if enablePartialTarget and wasInTrade and barstate.isconfirmed and not stopHit and not trendBreakExit" in source, "stop/structure exits must take priority over partial targets")
require("legRealizedPnlCcy" in source, "partial P&L must roll into its parent leg")
require("totalTrades = array.size(tradePnlCcy)   // completed legs;" in source, "statistics must count completed legs, not partial events")
require("feePctPerSide" in source and "slippagePctPerSide" in source and "fundingPctPer8h" in source, "configurable trading-cost assumptions must exist")
require("remainingEntryCost" in source and "remainingExitCost" in source and "remainingFundingCost" in source, "remaining-leg costs must be included at final exit")
require('Closed-leg drawdown (ccy)' in source, "drawdown label must distinguish closed-leg from mark-to-market drawdown")
require(source.count("array.push(tradePnlCcy,") == 1, "one completed-leg result must be recorded per leg")
require(source.count("array.push(tradePnlPct,") == 1, "one completed-leg percentage result must be recorded per leg")
require(source.count("array.push(tradeRMultiple,") == 1, "one completed-leg R result must be recorded per leg")
require(source.count("array.push(tradeDurationBars,") == 1, "one completed-leg duration must be recorded per leg")

print("Crypto Trend Rider static safety/accounting invariants passed.")
print("This does not compile Pine or validate exchange fills; use TradingView for that.")
