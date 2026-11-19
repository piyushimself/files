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
require("chartSeconds = timeframe.in_seconds()" in source and "chartSeconds != 14400" in source and "runtime.error(" in source, "script must reject non-4H chart intervals")
require('indicator("Crypto Trend Rider' in source, "script must remain explicitly labelled as an indicator simulation")
require("strategy(" not in source, "do not imply Strategy Tester execution")
require("barstate.isconfirmed and not wasInTrade and emaCrossUp" in source, "first entry must be confirmed-bar only")
require("barstate.isconfirmed and enablePyramidOnPullback" in source, "add entry must be confirmed-bar only")
require("barstate.isconfirmed and wasInTrade and not na(stopForBar) and low <= stopForBar" in source, "initial/trailing stop must be enforced on a confirmed bar")
require("math.max(chandelierLine[1], chandelierCandidate)" in source, "long Chandelier stop must ratchet and use prior stop")
require("barstate.isconfirmed and wasInTrade and (trendBreakExit or stopHit)" in source, "full exits must be confirmed-bar only")
require("high >= targetP" in source, "partial target must use an intrabar high touch")
require("maxval=99.0" in source, "partial target must not allow a zero-remaining open leg")
require("bar_index > array.get(legEntryBar, i)" in source, "new entries must not be partially exited on their entry bar")
require("if enablePartialTarget and wasInTrade and barstate.isconfirmed and not stopHit and not trendBreakExit" in source, "stop/structure exits must take priority over partial targets")
require("legRealizedPnlCcy" in source, "partial P&L must roll into its parent leg")
require("totalTrades = array.size(tradePnlCcy)   // completed legs;" in source, "statistics must count completed legs, not partial events")
require("feePctPerSide" in source and "slippagePctPerSide" in source and "spreadPctPerSide" in source and "fundingPctPer8h" in source, "configurable fee, slippage, spread and funding estimates must exist")
require("entryP * qtyV * (feePctPerSide + slippagePctPerSide + spreadPctPerSide)" in source, "entry-side costs must include spread")
require("fillPrice * scaleQty * (feePctPerSide + slippagePctPerSide + spreadPctPerSide)" in source, "partial-exit costs must include spread")
require("exitPrice * qtyRemain * (feePctPerSide + slippagePctPerSide + spreadPctPerSide)" in source, "final-exit costs must include spread")
require("remainingEntryCost" in source and "remainingExitCost" in source and "remainingFundingCost" in source, "remaining-leg costs must be included at final exit")
require('Closed-leg drawdown (ccy)' in source, "drawdown label must distinguish closed-leg from mark-to-market drawdown")
require(source.count("array.push(tradePnlCcy,") == 1, "one completed-leg result must be recorded per leg")
require(source.count("array.push(tradePnlPct,") == 1, "one completed-leg percentage result must be recorded per leg")
require(source.count("array.push(tradeRMultiple,") == 1, "one completed-leg R result must be recorded per leg")
require(source.count("array.push(tradeDurationBars,") == 1, "one completed-leg duration must be recorded per leg")

ath = (ROOT / "ATH_Weekly_Confirmed_Strategy.pine").read_text(encoding="utf-8")
legacy_ath = (ROOT / "ATH - Pine.txt").read_text(encoding="utf-8")

require(ath.startswith("//@version=5"), "ATH replacement must be Pine v5")
require('strategy("ATH Monthly Breakout / Weekly Execution Strategy v1"' in ath,
        "ATH replacement must be a Strategy Tester strategy")
require("timeframe.in_seconds()" in ath and "chartSeconds != 604800" in ath and "runtime.error(" in ath,
        "ATH strategy must reject non-weekly charts")
require('request.security(syminfo.tickerid, "M"' in ath and
        "lookahead=barmerge.lookahead_on" in ath and "open[1]" in ath and "close[1]" in ath,
        "ATH strategy must use previous confirmed monthly data without lookahead")
require("barstate.isconfirmed and newMonth" in ath,
        "monthly signals must be processed on confirmed weekly bars")
require("weeklyExit = barstate.isconfirmed" in ath and "strategy.close_all" in ath,
        "weekly SMA exit must execute on confirmed weekly closes")
require("strategy.exit(" in ath and "stop=stopPrice" in ath and "limit=target1" in ath and "limit=target2" in ath,
        "ATH stops and targets must be real strategy exit orders")
require("strategy.equity" in ath and "strategy.opentrades" in ath,
        "position sizing must use strategy equity and actual open legs")
require("cumEquityMult" not in ath and "cagrPct" not in ath and "tradePnlPct" not in ath,
        "remove custom per-leg compounded account metrics")
require("DEPRECATED" in legacy_ath and "ATH_Weekly_Confirmed_Strategy.pine" in legacy_ath,
        "old ATH indicator file must clearly point to its replacement")

print("Crypto Trend Rider static safety/accounting invariants passed.")
print("ATH weekly-strategy static safety checks passed.")
print("Static checks do not compile Pine or validate broker fills; use TradingView for that.")

require("Fee/slip/spread per side; funding per 8h" in source and "Fee / slip / spread / funding per 8h" not in source, "dashboard must distinguish per-side trading costs from 8-hour funding")
