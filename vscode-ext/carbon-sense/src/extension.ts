import * as vscode from 'vscode';
import { initStatusBar } from './statusBar';
import { registerChatParticipant } from './chatParticipant';
import {
	handleOptimizeCommand,
	handleOptimizeForCopilot,
	handleShowDashboard,
	handleResetSession,
	handleSetMemorySessionId,
	handleClearMemorySessionId,
} from './commands';

export function activate(context: vscode.ExtensionContext): void {
	console.log('Carbon Sense AI: activating...');

	initStatusBar(context);
	registerChatParticipant(context);

	context.subscriptions.push(
		vscode.commands.registerCommand(
			'carbon-sense.optimize',
			handleOptimizeCommand
		),
		vscode.commands.registerCommand(
			'carbon-sense.optimizeForCopilot',
			handleOptimizeForCopilot
		),
		vscode.commands.registerCommand(
			'carbon-sense.showDashboard',
			handleShowDashboard
		),
		vscode.commands.registerCommand(
			'carbon-sense.resetSession',
			handleResetSession
		),
		vscode.commands.registerCommand(
			'carbon-sense.setMemorySessionId',
			handleSetMemorySessionId
		),
		vscode.commands.registerCommand(
			'carbon-sense.clearMemorySessionId',
			handleClearMemorySessionId
		)
	);

	console.log('Carbon Sense AI: activated. Use @carbon-sense in Copilot Chat.');
}

export function deactivate(): void {
	// context.subscriptions handles cleanup
}
