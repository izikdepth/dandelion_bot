import discord
from discord.ext import commands
import logging





class Faq(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        
    @discord.slash_command(description="What is Dandelion?")
    async def aboutus(self, ctx):
        message = (
            "Dandelion (the network) is a secure, resilient, open, decentralized, computation platform,\n"
            "a network of independent computers (nodes) that come to consensus on the correct execution\n"
            "of transaction based computational tasks. 'Secure and resilient', means you can be sure the\n"
            "network will keep operating even if any of the nodes on it fail or act maliciously.\n"
            "Combined with 'open and decentralized', this means the network has the property of decentralized trust.\n"
            "You can trust the network, without trusting anyone on the network. Last, 'computation platform'\n"
            "means that Dandelion can carry out any computation task you care to program into it. Put it all\n"
            "together, and it means that code that runs on Dandelion is guaranteed to execute as written,\n"
            "regardless of what happens. Trustable transactions are the backbone of the network. They pay for\n"
            "the computational resources used (including themselves!) and enable the total network value to\n"
            "underpin external transactions as well.\n"
            "At its core, the Dandelion Network is as an autonomous, independent entity that operates as a\n"
            "universal public utility for trustable computing. The network provides trustable computing as a\n"
            "commodity in the same way that a decentralized electricity grid supplies secure, resilient power\n"
            "as a commodity.\n"
            "Dandelion (the company) is a small startup based in Toronto, and dedicated to bringing the Dandelion\n"
            "vision to the world."
        )
        await ctx.respond(message)
        
    
    @discord.slash_command(description ="What is Dandelion's vision?")
    async def ourvision(self, ctx):
        message = (
        "A world in which all 8 billion people have access to secure, resilient, trustable transaction services,"
        " regardless of geography or economic status."
        )
        await ctx.respond(message)
        
    @discord.slash_command(descritpion = "What is Dandelion's mission")
    async def mission(self,ctx):
        message = (
            "Dandelion will disrupt existing transaction networks in order to capture, enable global financial inclusion."
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="Why the name Dandelion?")
    async def name(self, ctx):
        message = (
            "Dandelions are humble, beautiful, and unstoppable.  We could not think of a better symbol for our vision, our company, and our people."
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="What are Dandelion’s roots?")
    async def roots(self, ctx):
        message = (
            "Dandelion is built on the heritage of open transaction systems, pioneered by Bitcoin and open computation, pioneered by Ethereum. "
            "These systems changed the world but face serious sustainability and efficiency problems. Paul Chafe and five of his students from George Brown College set out to find a better way. "
            "In collaboration with Atefeh Mashatan, director of the Cybersecurity Research Lab at Toronto Metropolitan University, they won a peer-reviewed research grant from the Mathematics, Information Technology, and Complex Systems (MITACS) Centre of Excellence, part of the Canadian government's National Centres of Excellence initiative. "
            "Alex Munro, a veteran of BNP Paribas, left a successful VC career to lead the team on the business and financial side. "
            "Today, the Dandelion team has twenty core members on three continents, but we are at heart a Toronto company, built around the students who came to do research and stayed to build the future. "
            "Our technical team includes three PhDs in electrical engineering, computer science, and mathematics, and our business advisory board contains several successful CEOs. "
            "We draft talent from the George Brown blockchain program, the Cybersecurity Research Lab at TMU, the University of Waterloo's computer engineering program, and the Computer Science Innovation Lab at the University of Toronto."
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="What does Dandelion look for in its people?")
    async def people(self, ctx):
        message = (
            "We screen for the ability to learn fast, entrepreneurial mindset, and strong leadership potential. "
            "People with this trilogy will learn what they have to learn, do what they have to do, to get done what they have to get done. "
            "More important, they will have a great time doing it and inspire others to come do it too. "
            "We built our culture before we built our product, and we love them both."
        )
        await ctx.respond(message)

    @discord.slash_command(description="How is Dandelion funded?")
    async def funding(self, ctx):
        message = (
            "To date, Dandelion's research and development has been funded with research grants issued by the nonprofit research organization Mathematics of Information Technology and Complex Systems (MITACS), which is in turn supported by the Government of Canada. "
            "This research is conducted through, and with the support of the blockchain program at George Brown College, and the Cybersecurity Research Lab at Toronto Metropolitan University. "
            "Other company operations have been funded by small investments from Revtech Lab Fintech Accelerator, from our founders, and from private individuals. "
            "Dandelion has not accepted venture capital funding at this time."
        )
        await ctx.respond(message)
        
    """
    ABOUT THE DANDELION NETWORK

    """
    @discord.slash_command(description="Why is decentralized trust important?")
    async def de_trust(self, ctx):
        message = (
            "As systems have grown more complex and connected, we have come to rely on them more and more. Today’s world is completely connected, but the systems we rely on are dangerously vulnerable to failure and even digital attack, at every level from the silicon up to the datacentre. Hacks and crashes cost us over a trillion dollars annually – and have cost lives as well. Open computation networks with the property of decentralized trust eliminate these vulnerabilities. Anyone can deploy and run code which is both fully transparent and is guaranteed to execute as-written and fairly. Coders still have to write their code correctly, but no-one can exploit the underlying system to make it run incorrectly."
        )
        await ctx.respond(message)

    @discord.slash_command(description="What can we use decentralized trust computing networks for?")
    async def use_of_decentralization(self, ctx):
        message = (
            "Anything! To date decentralized computation has been used mainly for transactions, as pioneered by Bitcoin. "
            "Transactions are just a specific form of computation, and they were the go-to application for early work in the field. "
            "Ethereum generalized this idea to include any computation, using transactions as inputs and outputs. "
            "Simple smart-contracts are the primary use-case on Ethereum and similar platforms, because their costs are so high. "
            "More complex applications can run in theory, but in practice are prohibitively expensive.\n"
            "Dandelion still does transactions (at tap-and-pay speed and global scale) – in fact, a transaction is the basic unit of both value transmission and data transmission on the network, the necessary first step in any trustable computation. "
            "However, we make trustable computation so efficient and so accessible that transactions are just the starting point. "
            "Dandelion can run secure messaging without a central server, operate social media networks that can’t harvest user data, run markets that cannot be front run or high-frequency-traded, support distributed wireless networks (so you can fire your phone company), provide artist-driven content delivery without middlemen, and much more. "
            "As with the early internet, the applications weren’t even imaginable when the technology first launched."
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="How fast is Dandelion?")
    async def speed(self, ctx):
        message = (
            "Really fast!  On a high-speed 5G connection, you can complete a tap-and-pay transaction in under a second.  "
            "The network as a whole can handle over a quarter million of those transactions every second, "
            "on ordinary desktop servers with good bandwidth.  More importantly, Dandelion scales naturally with demand.  "
            "This is an important distinction from systems like Bitcoin, which cannot scale natively and so must use “Layer 2” solutions that inevitably compromise security in search of speed.  "
            "In fact, Dandelion is faster on Layer 1 than Bitcoin Lightning, Ethereum Plasma, and even Polygon are on layer 2."
        )
        await ctx.respond(message)
        
    
    @discord.slash_command(description="How efficient is Dandelion?")
    async def efficiency(self, ctx):
        message = (
            "Really efficient!  In fact, we believe Dandelion is the most efficient decentralized network that can exist.  "
            "Like all open decentralized systems, Dandelion is Asynchronous Byzantine Fault Tolerant (ABFT). This means the network will work properly as long as a majority of its nodes act honestly.  "
            "However, fault tolerance comes at a cost.  In a pure-peer network, the number of messages needed to come to consensus rises proportional to the square of the number of nodes because every node has to update every other node at every consensus cycle.  "
            "This becomes untenable long before there are enough nodes to consider the network effectively decentralized.  "
            "Systems built on Proof-of-Work and Proof-of-Stake use a single leader to decide on consensus, after which every other node simply has to agree that the decision is correct.  "
            "This reduces the co-ordination cost to simply proportional to the number of nodes but comes with another cost. These systems deliberately waste vast amounts of electrical or economic power in the race to win the leader election.  "
            "This makes them slow and expensive (also environmentally and economically unsustainable).\n"
            "On Dandelion, the network's clients are responsible for leading their transactions and handling all the messages necessary for consensus.  "
            "Dandelion nodes don't have to message to each other at all to complete a simple transaction (there is some communication necessary for network-level housekeeping). They are then free to devote all their time and bandwidth to servicing clients."
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="What makes Dandelion special")
    async def what_makes_us_special(self, ctx):
        message = (
            "It's fast enough to do peer-to-peer tap-and-pay, it's smart enough to do pay-a-contact through client-integrated secret messaging, "
            "it scales naturally with demand, and it will run the Decentralized Data Centre.  They key to all this is computational efficiency.  "
            "In fact, we believe Dandelion is the most efficient decentralized computation that can exist.  Efficiency is important because currency is a technology, and over time, the most efficient technology dominates.  "
            "This is why we cross oceans in airliners, not steamships."
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="What is the Decentralized Data Centre")
    async def de_data_center(self, ctx):
        message = (
            "Transactions and smart contracts (which have transactions as inputs and outputs) need to run with the full decentralized security of the network.  "
            "Anything less simply isn't safe (it should be noted, Layer 2 systems accept this risk, and this is why they're a bad idea).  "
            "However, there are lots of applications that need some level of redundancy, but not quite the full security of the network.  "
            "The Decentralized Data Centre provides this - computation, storage, and bandwidth, available on demand, to do whatever you want with.  "
            "Imagine AWS or Microsoft Azure - but with a large corporation telling you what you can or cannot run."
        )
        await ctx.respond(message)

    """"
    USING DANDELION 

    """
    @discord.slash_command(description="What wallets can I use with Dandelion?")
    async def wallets(self, ctx):
        message = (
            "The best wallet is our Breeze App, which integrates tap-and-pay and pay-a-contact with through-chain secure secret messaging.  However we are integrating with other wallets, with browser and hardware platforms as the priority"
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="Can I use Dandelion for online microtransactions?")
    async def micropayments(self, ctx):
        message = (
            "Yes!  The Dandelion network is ideally suited for online microtransactions, due its high speed, low cost, and fast finalization time." )
        await ctx.respond(message)
        
    @discord.slash_command(description="Can I tap-and-pay with Dandelion?")    
    async def tap_and_pay(self, ctx):
        message = (
            "Yes!  Our Dandelion Breeze App runs on your phone, and does Tap-and-Pay over-the-counter, and out-of-the-box."
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="Can I tap-and-pay card-to-phone?")
    async def card_to_phone(self, ctx):
        message = (
            "We have card-to-phone payments on our roadmap, using next-generation smart-cards with integrated biometric security."
        )  
        await ctx.respond(message)
        
    @discord.slash_command(description="Can I snap-and-pay code-to-phone?")
    async def code_to_phone(self, ctx):
        message = (
            "Yes!  With Breeze you can use simple QR-codes to request, initiate, and complete any payment. "
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="Can I pay-a-contact with Dandelion")   
    async def pay_contact(self, ctx):
        message = (
            "Yes!  Breeze includes secure, End-to-End encrypted messaging done through the network.  You can send a transaction to anyone in your contact list, peer-to-peer and with complete security."
        ) 
        await ctx.respond(message)
        
    @discord.slash_command(description="Why will people accept Dandelion payments?")
    async def why_use_dandelion(self, ctx):
        message = (
            "Dandelion coins give access to units of trustable computation.  Even if your counterparty don’t need this service, lots of people do.  This gives them the confidence that they can accept Dandelion, because they know they can trade it away later.  This actually works the same way gold and silver work."
        )
        await ctx.respond(message)
        
    """SECURITY"""
    
    @discord.slash_command(description="Can valid Dandelion transactions always complete?")
    async def can_transactions_complete(self, ctx):
        message = (
            "Yes! In concurrent systems theory, a system which is live will always be able to make computational progress. "
            "It has neither deadlocks nor livelocks. In other words, valid transactions will always be able to complete. "
            "To prove this, we built a mathematical model of Dandelion using TLA+, a formal math system built by Leslie Lamport, "
            "one of the pioneers of the field. We ran this model for two weeks on the University of Toronto's Niagara supercomputer, "
            "visiting every state network could enter (over a trillion in total). This conclusively demonstrated that the system has no "
            "deadlock or livelock states. Valid transactions can always complete given a majority of honest nodes, so long as the clients "
            "do the work to complete them. As a bonus - we got to use a supercomputer!"
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="Will invalid Dandelion transactions always fail?")
    async def can_invalid_transactions_fail(self, ctx):
        message = (
            "Yes! In concurrent systems theory, a system which is safe will not allow unintended states to happen. "
            "In Dandelion's case, we want the system to be Asynchronous, Byzantine, Fault Tolerant (ABFT), which means that the "
            "safety property must hold even if messages can be lost or indefinitely delayed, nodes can drop on and off the network at random, "
            "and even if nodes behave maliciously, lying about their own state or the state of other nodes. To prove this, we built a "
            "provable security model of Dandelion. This is a mathematical analysis technique in which we formalized the capabilities of an "
            "adversary who might be trying to break the system. This analysis proved that invalid transactions will always fail, given a majority "
            "of honest nodes, and regardless of what a malicious adversary does or how powerful it is. This was published as the lead article "
            "in the 2022 Cybersecurity issue of the peer-reviewed journal Mathematics. We're very proud of it."
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="Can Dandelion be Sybil-attacked?")
    async def can_be_sybil_attacked(self, ctx):
        message = (
            "No. A Sybil-attack happens when an attacker is able to inexpensively add enough nodes to the network "
            "to overwhelm consensus. Dandelion consensus is designed to decentralize, and does not allow Sybil attack."
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="What is the kill-switch?")
    async def what_is_kill_switch(self, ctx):
        message = (
            "The kill-switch is a backup public/private keypair, generated at the same time as a node's operational keypair. "
            "The kill-switch public key is linked with the operational public key on the network, but the kill-switch private key is held securely offline. "
            "If someone steals the node's operational private key, the kill-switch private key can be used to tell the network and disable the operational public key. "
            "The kill-switch keypair becomes operational, and a new kill-switch keypair is generated."
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="What is distributed key recovery?")
    async def what_is_distributed_key_recovery(self, ctx):
        message = (
            "Distributed key recovery is a way of making your private key disaster-resilient, by splitting it into several parts and storing those parts "
            "in widely separated locations (e.g., a bank vault, with trusted friends, with your lawyer, etc). The neat part is, you can configure the split key "
            "so that you don't need all the parts to recover your private key. For example, with ten parts, you could use any five to recover them."
        )
        await ctx.respond(message)

    @discord.slash_command(description="What are identicons?")
    async def what_are_identicons(self, ctx):
        message = (
            "Today, cryptocurrency addresses are long strings of hexadecimal. They are hard to read, and easy to make mistakes with, "
            "which makes them user-unfriendly. Dandelion's Breeze app uses a special algorithm to turn a Dandelion wallet address into a unique, "
            "visual symbol, kind of like a digital flower. The algorithm is set up so that a single change to an address produces a radically different symbol. "
            "The human eye is very good at picking up visual differences like this, which makes mistakes immediately visible. This kind of user-friendly security "
            "is built into everything we do and is essential if peer-to-peer transactions are to become the default mode of value transfer for everyday use."
        )
        await ctx.respond(message)

    """TECHNOLOGY"""
    
    @discord.slash_command(description="How is Dandelion better?")
    async def how_is_dandelion_better(self, ctx):
        message = (
            "In a simple peer-to-peer network, every node has to update every other node on every step of consensus. The number of messages required rises as the square of the number of nodes (O(n^2), "
            "and quickly reaches an unworkable volume, no matter how much bandwidth you throw at the problem. Networks like Bitcoin and Ethereum improve on this by electing a leader (either through work done or stake committed). All communications go through the leader, which is rotated block by block. "
            "This reduces the communications burden to simply proportional to the number of nodes (O(n)) which is better. However, these proofs waste a lot of electrical or economic power, forces the unscalable, serial blockchain structure, and leads to vulnerabilities like in-block front-running and empty block mining."
            "Dandelion uses the fully parallel blocklattice structure, asynchronous clear and settle, and the client-leader consensus architecture. Dandelion's communication burden is flat (O(1)), regardless of the number of nodes on the network. More important, Dandelion scales with demand, with a built-in upgrade incentive for nodes. The network will always be driven towards the point where computational cost meets demand. In fact, we believe Dandelion is the most efficient decentralized network that can exist."
        )
        await ctx.respond(message)

    @discord.slash_command(description="What is parallelism, and why is it important?")
    async def what_is_parallelism(self, ctx):
        message = (
            "Parallel systems can do many things at once, where serial systems can only do one thing at a time.  Conventional blockchains are inherently serial structures – literally a chain of cryptographically linked blocks, built one link after another.  Dandelion uses a blocklattice, a fabric of many threads, all advancing simultaneously.  This eliminates the bottleneck that makes blockchain slow and expensive, without the security compromises that have seen so many “layer two” and similar solutions get hacked. "
        )
        await ctx.respond(message)

    @discord.slash_command(description="What is asynchronicity, and why is it important?")
    async def what_is_asynchronicity(self, ctx):
        message = (
            "Synchronous systems move in lockstep, like an assembly line.  If a single component stops, the entire system has to wait until it catches up– a situation known as blocking in computer science.  Asynchronous systems are like a swarm of bees.  The hive as a whole is co-ordinated, but each bee works on its own.  Dandelion does this by splitting each transaction into two parts.  A transaction is cleared when a sending client commits funds to a specific receiver, and then settled when the receiving client orders those funds in its own account (note the specific order doesn't matter, as all receipts are additions.  Because these operations are separated, the network is non-blocking.  "
        )
        await ctx.respond(message)

    @discord.slash_command(description="What is Client-Leader and why is it important?")
    async def what_is_client_leader(self, ctx):
        message = (
            "For a simple consensus network, every node must agree on every transaction – this is what creates decentralized trust. The drawback is that every node has to talk to every other node to reach consensus, and the number of connections required to reach consensus rises proportional to the square of the number of nodes. To get around this, networks like Bitcoin and Ethereum use a leader-election system. One node is elected to decide what transactions should be processed, and then tells the rest of the nodes. These nodes simply verify that what the leader decided was correct. Proof-of-Work and Proof-of-Stake are simply leader election systems that incentivize the leader to decide -mostly-honestly.\n\n"
            "This reduces the communication burden to merely linear with the number of nodes, but creates two more issues. The leader is in a privileged position, and its decisions can favor itself. This shows up in practices like empty block mining and miner-extracted value, both now common features of conventional blockchain mining. This reaps extra rewards for the leader node at the expense of the network as a whole. The larger problem is that the leader is itself a bottleneck, which strictly limits the number of transactions that can be processed.\n\n"
            "Client-Leader solves this problem by recognizing that clients have an inherent interest in completing their own transactions. Each client is the leader of its own thread of the blocklattice, clearing and settling transactions (asynchronously) as required. On Dandelion, the nodes don’t talk to each other at all to handle a simple transaction. The coordination and rebroadcast function is handled entirely by the client. The bandwidth burden at the node is constant no matter how many nodes are on the network."
        )
        await ctx.respond(message)

    @discord.slash_command(description="What is Demand Scaling and why is it important?")
    async def what_is_demand_scaling(self, ctx):
        message = (
            "We’d like to see a day when all eight billion people on our shared planet can do all the transactions they want, free of monopolized payment rails, "
            "free of fiat inflation, and enabled to create whatever decentralized-trust-guaranteed applications they want. We’d like to see them use those applications with privacy, "
            "accountability, and security baked in. In order to achieve this goal, the trust platform they use must be able to scale to hundreds of thousands, millions, "
            "tens of millions of transactions, every second. Anything less simply won’t do.\n\n"
            "The parallel, asynchronous, client-led architecture lets Dandelion scale in three ways. The blocklattice scales just by adding more threads. The network scales "
            "by adding blocklattices as required. Most importantly, Dandelion scales with demand. A client needs a 2/3+1 consensus to advance a transaction, and the slowest 1/3-1 of nodes "
            "will get left out of consensus - and consensus rewards - if they aren't fast enough to service the client-determined time constraint. As demand grows, nodes are incented to upgrade "
            "their capacity to keep up. No other network can scale like this."
        )
        await ctx.respond(message)

    @discord.slash_command(description="What is Fair Ordering and why is it important?")
    async def what_is_fair_ordering(self, ctx):
        message = (
            "It is possible to trust unfair systems, as long as they are consistently unfair.  Stock exchanges work, even though high frequency traders, brokers, and other privileged players use their privilege to siphon value from simple customers.  Blockchains work despite miner extracted value, in-block frontrunning and other leader-exploitation techniques open to miners but not users.  However this creates market inefficiency, because otherwise profitable trades do not get made when their marginal value doesn’t exceed the value that may be siphoned. Dandelion smart contracts use Fair Ordering, which guarantees that no transaction can be prioritized over another in smart contract execution."
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="What language are Dandelion Smart Contracts written in?")
    async def dandelion_sc_language(self, ctx):
        message = (
            "Dandelion uses a variation of WASM called adWASM (asynchronous, deterministic WASM), which is designed for parallel operation.  Any language that compiles to WASM can be used with a little tweaking, but we have a visual drag-and-drop coding environment designed to make it fast and easy to build adWASM smart contracts, taking maximum advantage of adWASM parallelism with a minimum of errors.  "
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="Can Dandelion be sharded?")
    async def dandelion_sharding(self, ctx):
        message = (
            "Yes!  Dandelion can easily operate any number of shards.  This enables scaling beyond demand scaling"
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="Is Dandelion open source?")
    async def opensource(self, ctx):
        message = (
            "Dandelion’s source code will be released on main-net launch.  Anyone will be able to download it, run a node, and modify it as they like, for free, and forever."
        )
        await ctx.respond(message)
    
    @discord.slash_command(description="What kind of nodes does Dandelion have.")    
    async def get_dandelion_node_info(self, ctx):
        message = (
            "Dandelion has only one kind of node, consisting of a public/private keypair, an independent copy of the blocklattice, "
            "and the software to run the Dandelion state machine and so advance transactions.  However there are several additional modules "
            "that nodes can choose to run as they are also payable services.  This includes decentralized storage, decentralized computation, "
            "decentralized bandwidth, and transaction delegation services.  Depending on the demand and services it provides, "
            "a Dandelion node can be a single physical machine, a cluster of several, or more."
        )
        await ctx.respond(message)
        
    """ECONOMICS"""
    
    @discord.slash_command(description="What is the Dandelion economic model?")
    async def economic_model(self, ctx):
        message = (
            "The Dandelion Network provides secure, resilient computation as a commodity resource to the world, just as a distributed electrical grid provides electricity.  Dandelion tokens let you use this resource, the same way bus tokens let you ride the bus.  New tokens are minted by nodes, who are rewarded for participating in consensus, and burned when they are used to complete transactions or computational tasks (for eg, executing smart contracts)  This is quite different from typical, fixed cap systems found in conventional blockchains.  The dynamics are designed to encourage adoption, encourage use, while growing the supply to a stable level, avoiding the instability that plagues existing systems.  The idea is to maximize the rate of network value growth, rather than the product of token volume and token value."
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="Does Dandelion use Proof of Stake?")
    async def is_ddln_pos(self, ctx):
        message = (
            "Not at all.  Proof-of-Stake is fiat currency to Proof-of-Work's gold.  Rewards flow to stakeholders, who are then incented to reward themselves more, creating inflation.  The rich get richer, the network centralizes, decentralized trust is lost.  PoS is outwardly more efficient than PoW, but the economic power locked up in stake is largely generated by electrical power (and fossil fuels), and so it remains inherently wasteful.  We don't think this is a good idea."
        )
        await ctx.respond(message)
    
    @discord.slash_command(description="Does Dandelion use Proof of Work?")
    async def is_ddln_pow(self,ctx):
        message = (
            "Yes, but not the way it's usually implemented.  Proof of Work works by encapsulating energy in a verifiable token – This is what made gold the literal gold-standard for over six-thousand years – gold was the most efficient verifiable energy encapsulator available to the ancient world.  However, where conventional blockchain Proof of Work presents nodes with an open-ended race to waste electrical power on hashing (an unsustainable model in the modern world), Dandelion uses the completion of computational tasks (including transactions) for users.  This work directly provides a useful service, and it uses only the energy required to complete the computation.  As a result Dandelion is orders of magnitude more efficient than Bitcoin and similar systems.  There is more to it than simple computation, but that's it in a nutshell."
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="Do Dandelion nodes compete for rewards?")
    async def check_reward_competition(self, ctx):
        message = (
            "Yes, Dandelion nodes compete for the opportunity to offer computation and transaction services to clients. "
            "This competition is structured much like a gold rush. Initially, there are a small number of high-quality sites. "
            "As the network evolves, the quality may decline, but the number of sites available increases. "
            "This approach fairly balances risk and payoff, rewarding early adopters while still providing an incentive for people to join later on. "
            "It steadily drives decentralization as the competition continues."
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="How fast will Dandelion decentralize?")
    async def dandelion_decentralization(self, ctx):
        message = (
            "As with all things Dandelion, the decentralization schedule is dynamic. "
            "As demand goes up, more nodes will be able to join the network. "
            "The best thing to do to help decentralize is to generate demand. "
            "As a very rough rule of thumb, node count will double every year. "
            "However, remember that later nodes will require more effort for the same reward, reflecting the lower risk they must accept in joining an already-established network."
        )
        await ctx.respond(message)

    @discord.slash_command(description="Are Dandelion economics inflationary or deflationary?")
    async def dandelion_economics(self, ctx):
        message = (
            "Economics are only inflationary or deflationary in a given context. "
            "Dandelion’s context is the global demand for secure, resilient computation, which is growing rapidly. "
            "Within that context, Dandelion's mint/burn system is aimed at maximizing the growth of network value rather than the product of token value and token supply. "
            "This shift in emphasis is what will allow us to rapidly pass established systems in value provided."
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="How do Dandelion nodes get rewarded?")
    async def dandelion_reward_system(self, ctx):
        message = (
            "Sending clients pay a small fee for each transaction, or more broadly, each computational task. "
            "This fee is burned. Simultaneously, the nodes which participate in consensus are paid a reward in new-minted coins. "
            "Note that the fee paid and the reward granted are not necessarily the same amount. "
            "This allows the network to automatically adjust the total coin volume to demand. "
            "More demand reduces coin flow, increasing the external coin price, and triggering the scaling incentive. "
            "As network capacity scales up, coin demand falls in relation to it. More coins are produced, and the external price optimizes to maximize use (and so value provided) at the new, higher capacity. "
            "The idea is to maximize the rate of increase of value provided by the network, rather than simply the product of coin price and coin volume."
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="How are Dandelion Tokens made available?")
    async def dandelion_tokens_availability(self, ctx):
        message = (
            "They will be available OTC (Over The Counter), and on several exchanges."
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="What is the coin generation schedule?")
    async def coin_generation_schedule(self, ctx):
        message = (
            "Coins are introduced into the system on an exponentially declining curve that begins with (nominally) ten million generated in the first year, declining by 20% per year to an approximate of fifty million in thirty years. "
            "Note that this is the baseline rate given average network demand as measured against supply at any given moment. "
            "In detail, Dandelion uses a decoupled mint/burn system that dynamically adjusts supply flow to balance demand, removing volatility. "
            "The idea is to ensure the marginal value of a single coin to be a constant function of risk, reward, and utility, in order to reward early adopters while continuing to incentivize adoption and use along the entire curve."
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="What is the demand tariff?")
    async def demand_tariff(self, ctx):
        message = (
            "Dandelion dynamically allocates sets the price for transactions and computations based on a number of factors. "
            "As demand increases towards total network capacity, the cost of transactions and computation increases non-linearly. "
            "Under normal load, this has no significant impact on operation. Under natural demand spikes, prices rise and fall smoothly. "
            "However, if a malicious attacker attempts a transaction flooding attack, it quickly becomes ruinously expensive for them, while having minimal impact on normal users. "
            "For example, if the network saturates at a quarter million transactions per second, and normal demand is half that, then normal transactions will cost a very small fraction of a penny. "
            "However, if an attacker floods the network, transaction fees will rise rapidly. "
            "If they are $0.10 at 90% capacity and a $1.00 at 99% capacity, the attacker must pay somewhere between $12,500 and $125,000 per second to sustain the attack! "
            "Meanwhile, normal users can easily afford this fee increase for the few transactions they will complete until the attacker runs out of funds - or they can simply wait until the attack is over. "
            "This is perhaps the only cyberattack a network could welcome!"
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="What is dynamic pricing?")
    async def dynamic_pricing(self, ctx):
        message = (
            "Dandelion can be thought of as an autonomous entity, providing transaction and computation services with the property of decentralized trust to the world. "
            "Computation can broadly be measured in storage used, bandwidth transmitted, and opcodes processed. "
            "All of these have different costs, and the cost will differ across the various nodes that make up the network, and are used to different degrees. "
            "The network is able to dynamically adjust the price of each service to ensure they are accurately priced with respect to both their underlying average cost and the relative demand."
        )
        await ctx.respond(message)
        
    """LAUNCH"""
    @discord.slash_command(description="What are the deployment phases of Dandelion?")
    async def deployment_phases(self, ctx):
        message = (
            "Dandelion will stage deployment through testnet and mainnet phases. Both testnet coins and nodes will transition to mainnet after we have proven network stability."
        )
        await ctx.respond(message)
    
    @discord.slash_command(description="Will testnet coins have value?")
    async def testnet_coins(self, ctx):
        message = (
            "Testnet nodes will operate live, and testnet coins will have value (after all, they give access to an operating service). They will initially be available to developers and others through a faucet and OTC. We are talking to several exchanges now for early listing, with one exchange confirmed."
        )
        await ctx.respond(message)
    
    @discord.slash_command(description="Will testnet coins transition to mainnet?")
    async def testnet_transition(self, ctx):
        message = (
            "Yes! Testnet coins and nodes will transition to mainnet."
        )
        await ctx.respond(message)
    
    @discord.slash_command(description="Will testnet nodes transition to mainnet?")
    async def fair_launch_testnet(self, ctx):
        message = (
            "Yes! We will be holding an open auction for testnet node positions. Anyone can join the auction, and we are working to make sure it is widely available to the crypto community."
        )
        await ctx.respond(message)
    
    @discord.slash_command(description="Will mainnet be fair-launched?")
    async def fair_launch_mainnet(self, ctx):
        message = ("Yes, on mainnet all nodes will have to compete to participate in consensus, including all testnet nodes. Testnet operators gain skill and experience in the competition, at the cost of up-front risk and effort. However winning a place in consensus requires competing on a level field, and the decentralization mechanism is always opening up new opportunities for new entrants.")
        await ctx.respond(message)
        
    @discord.slash_command(description="Why would I buy a testnet node at auction if I can get a node for free on mainnet launch?")
    async def why_buy_testnet_node(self, ctx):
        message = (
            "Remember the Dandelion proof protocol works like a gold rush. "
            "Earlier arrivals have an easier time finding a site, and sites found later will take more effort to earn the same reward (trading off the lower risk of waiting before investing). "
            "On mainnet launch, anyone can download and run the software - and we hope a lot of people do. "
            "However, not everyone (in fact, not most people) will be to win a place in consensus, and the reward rate is lower the later you join. "
            "As with the coin generation schedule, the intent is to provide a constant function of risk, reward, and utility. "
            "This is what makes it worth investing in testnet participation."
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="When will the auction be held?")
    async def auction_date(self, ctx):
        message =  ("Late 2023.")
        await ctx.respond(message)
        
    @discord.slash_command(descriprion="How many nodes will operate on testnet?")
    async def testnet_nodes(self, ctx):
        message = ("There will be 128 nodes on testnet.")
        await ctx.respond(message)
        
    @discord.slash_command(description="How long will testnet run?")
    async def testnet_duration(self, ctx):
        message = ("We are targeting four months, but will run as long as necessary to resolve any issues.")
        await ctx.respond(message)
        
    @discord.slash_command(description="How many nodes will the Dandelion team retain?")
    async def team_nodes(self, ctx):
        message = (
            "This depends on how the auction goes, but in all cases Dandelion will retain a sub-consensus fraction of nodes.  This is necessary for the decentralized trust property to hold."
        )
        
        await ctx.respond(message)
        
    @discord.slash_command(description="Are there any premined coins?")
    async def premined_coins(self, ctx):
        message = (
            "No.  All coins will be minted on both testnet and on mainnet."
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="How many coins will the Dandelion-owned nodes get during testnet phase?")
    async def owned_coins(self, ctx):
        message = (
            "This also depends, on both auction results and the duration of testnet, but 5% of total supply is a conservative maximum"
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="Will Dandelion coins be available to developers and community?")
    async def availability_dev_community(self, ctx):
        message = (
            "We are starting a Dandelion foundation to handle the distribution of coins to encourage development on Dandelion. "
            "The foundation will actively support development of new applications, "
            "and the porting of old applications to run (better) on Dandelion."
        )
        await ctx.respond(message)
        
    
    """COMPANY"""
    @discord.slash_command(description="Can I invest in Dandelion?")
    async def invest_in_dandelion(self, ctx):
        message = (
            "Can I invest in Dandelion?\n"
            "Dandelion, the company is not publicly traded and there are no plans to become publicly traded at this time.\n"
            "Dandelion, the coin, is a computational ticket-to-ride on the Dandelion network, and its value springs from the value of this service to the world. "
            "The high speed, low cost, and convenience of Dandelion transactions means this value easily intermediates trades between counterparties. "
            "Dandelion is built to be used, and every transaction you make adds value to the network.\n"
            "Dandelion, the network is made of nodes. People interested in running a node can bid for a node slot during the testnet auction (and we hope you do), "
            "but this is not an investment in Dandelion. Running a node is a competitive business. "
            "We will do all we can to set you up for success, but the results are up to you.\n"
            "Dandelion, the community, is the best place to create decentralized applications we can imagine. "
            "Investing in building these applications, and the people who build them, is a tremendous opportunity. "
            "The more you use the network, the more value it has, and so the more value Dandelion coins have. "
            "It takes a village to raise a child, and a community to create the decentralized future."
        )
        await ctx.respond(message)
        
    @discord.slash_command(description="Does Dandelion have Venture Capital(VC) backing?")
    async def vc_backing(self, ctx):
        message = (
            "No. To date we have done everything with peer-reviewed research grants, team investment, and a small amount of investment from private individuals "
            "and the Revtech fintech accelerator. This approach has allowed us to build value without no pressure to meet artificial deadlines. "
            "We are open to accepting VC if it makes sense for the company, the community, and the network."
        )
        await ctx.respond(message)


    @discord.slash_command()
    async def whitepaper(self, ctx):
        message = "[Read our whitepaper](https://dandelionnet.io/wp-content/uploads/2022/09/dandelion_whitepaper.pdf)"
        await ctx.respond(message)
  
        
    @discord.slash_command()
    async def website(self, ctx):
        message = "[Website](https://dandelionnet.io/)"
        await ctx.respond(message)
    
    @discord.slash_command()
    async def community(self, ctx):
        message = ("[Reddit](https://www.reddit.com/user/Dandelion_Networks/)\n"
                   "[Telegram](https://t.me/+laYlUWRjDks1MWYx)\n"
                   "[Tiktok](https://www.tiktok.com/@ddln_networks)\n"
                   "[Linkedin](https://www.linkedin.com/company/dandelionnetworks/)\n"
                   "[Twitter](https://twitter.com/ddln_networks)\n"
                   "[Medium](https://dandelionnetworks.medium.com/)\n"
                   "[Youtube](https://www.youtube.com/channel/UCzS_dKW5Z0xJOnAGmA_2oXQ)"
                   )
        await ctx.respond(message)
    
    # @discord.slash_command()
    # async def node(self, ctx):
    #     message = "[#node-setup](https://discord.com/channels/1027371612875542588/1107803939283406878)"
    #     await ctx.respond(message)


    @discord.slash_command()
    async def exchanges(self, ctx):
        message = "[#exchanges](https://discord.com/channels/1027371612875542588/1108085988384841808)"
        await ctx.respond(message)
        
    @discord.slash_command()
    async def roadmap(self, ctx):
        message = ("Estimates:\n\n"
                   "Q3-Q4 2023 test nodes.\n"
                   "Q4 2023-Q1 2024 public nodes.\n"
                   "2024-2025 exchanges - tentatively txbit, tradeogre, mexc or kucoin \n"
                   "[more](https://discord.com/channels/1027371612875542588/1108085988384841808/1108086095528333383)")
        await ctx.respond(message)
        

    
    
"""
set up bot and register the cog to the bot
"""
def setup(bot):
    bot.add_cog(Faq(bot))
