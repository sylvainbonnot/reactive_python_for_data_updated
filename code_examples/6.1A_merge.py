import reactivex as rx

source1 = rx.from_(["Alpha", "Beta", "Gamma", "Delta", "Epsilon"])
source2 = rx.from_(["Zeta", "Eta", "Theta", "Iota"])

rx.merge(source1, source2).subscribe(print)
