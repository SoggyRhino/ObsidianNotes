---
date created: 2025-02-12 14:57
---

Hi, I just joined and I think I found the cause.

[Page.ClientNavigationReason](https://chromedevtools.github.io/devtools-protocol/tot/Page/#type-ClientNavigationReason) is marked as Experimental in the CDP and it looks like `initialFrameNavigation` value was only recently added to the spec.

Cdproto added it on August 14, 2024 with [Commit b931b75](https://github.com/chromedp/cdproto/commit/b931b754e476202efa174f06c427a270018c52e6)

```go
const (
	ClientNavigationReasonAnchorClick            ClientNavigationReason = "anchorClick"
	ClientNavigationReasonFormSubmissionGet      ClientNavigationReason = "formSubmissionGet"
	ClientNavigationReasonFormSubmissionPost     ClientNavigationReason = "formSubmissionPost"
	ClientNavigationReasonHTTPHeaderRefresh      ClientNavigationReason = "httpHeaderRefresh"
	ClientNavigationReasonInitialFrameNavigation ClientNavigationReason = "initialFrameNavigation"
	ClientNavigationReasonMetaTagRefresh         ClientNavigationReason = "metaTagRefresh"
	ClientNavigationReasonOther                  ClientNavigationReason = "other"
	ClientNavigationReasonPageBlockInterstitial  ClientNavigationReason = "pageBlockInterstitial"
	ClientNavigationReasonReload                 ClientNavigationReason = "reload"
	ClientNavigationReasonScriptInitiated        ClientNavigationReason = "scriptInitiated"
)

// MarshalEasyJSON satisfies easyjson.Marshaler.
func (t ClientNavigationReason) MarshalEasyJSON(out *jwriter.Writer) {
	out.String(string(t))
}

// MarshalJSON satisfies json.Marshaler.
func (t ClientNavigationReason) MarshalJSON() ([]byte, error) {
	return easyjson.Marshal(t)
}

// UnmarshalEasyJSON satisfies easyjson.Unmarshaler.
func (t *ClientNavigationReason) UnmarshalEasyJSON(in *jlexer.Lexer) {                   // <-this is were the error is coming from
	v := in.String()
	switch ClientNavigationReason(v) {
	case ClientNavigationReasonAnchorClick:
		*t = ClientNavigationReasonAnchorClick
	case ClientNavigationReasonFormSubmissionGet:
		*t = ClientNavigationReasonFormSubmissionGet
	case ClientNavigationReasonFormSubmissionPost:
		*t = ClientNavigationReasonFormSubmissionPost
	case ClientNavigationReasonHTTPHeaderRefresh:
		*t = ClientNavigationReasonHTTPHeaderRefresh
	case ClientNavigationReasonInitialFrameNavigation:
		*t = ClientNavigationReasonInitialFrameNavigation
	case ClientNavigationReasonMetaTagRefresh:
		*t = ClientNavigationReasonMetaTagRefresh
	case ClientNavigationReasonOther:
		*t = ClientNavigationReasonOther
	case ClientNavigationReasonPageBlockInterstitial:
		*t = ClientNavigationReasonPageBlockInterstitial
	case ClientNavigationReasonReload:
		*t = ClientNavigationReasonReload
	case ClientNavigationReasonScriptInitiated:
		*t = ClientNavigationReasonScriptInitiated

	default:
		in.AddError(fmt.Errorf("unknown ClientNavigationReason value: %v", v))
	}
}
```

Chromedp version 10.0.0 (what we are using) requires 	Cdproto v0.0.0-20240801214329-3f85d328b335, which was released August 1, 2024.

Chromedp versions 10.0.1+ use updated versions of Cdproto

Basically we just need to update Chromedp, I tested with the latest version (12.0.1) and the errors were gone.
